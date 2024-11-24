import glob
import logging
from dataclasses import fields
from datetime import datetime

import pandas as pd

from data.model.stock import Stock, MarketCapType, MarketCap
from data.stock.constants import COL_NAMES, MARKET_CAP_STR
from data.stock.my_secrets import STOCK_WATCHLIST_PATH

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def extract_column(file: str, col: str):
    """extra all rows for one column, comma delimited"""
    df = pd.read_csv(file, header=2, index_col=False, skipfooter=30, engine='python')
    # print(df.columns)
    # print(df[col].tolist())
    # print(df.shape)
    # print(df.head())  # summary with first 5 rows
    return df[col].tolist()


def extract_col_to_list_glob(path: str):
    """extract one column from multiple csv files"""
    res = set()
    for f in glob.glob(path + '/*.csv'):
        res.update(extract_column(f, 'Symbol'))
    logger.info(f'total stocks in watchlist: {len(res)}')
    return list(res)


def save_watchlist():
    # extract stock tickets from watchlist csv export, keep in Google Drive
    with open('stock_list.txt', 'w') as f:
        stocks = extract_col_to_list_glob(STOCK_WATCHLIST_PATH)
        logger.debug(f'write 50 tickers per line')

        def chunks(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i:i + n]

        list_of_lists = chunks(stocks, 50)
        f.write('\n'.join(','.join(l) for l in list_of_lists))


def p2f(s: str) -> float:
    """percentage to float, 1.1% -> 0.011"""
    return float(s.strip('%')) / 100


def d2f(s: str) -> float:
    """$ dollar value str to float, $2.3 -> 2.3"""
    return float(s.replace('$', ''))


def get_rating(s: str) -> float:
    """str to float rating, Bullish (8.4) -> 8.4"""
    return float(s[-4:-1])


def get_market_cap(s: str) -> MarketCap:
    """str to market cap, Mega Cap ($3.40 T) -> (MEGA(4),3.4)"""
    dollar_idx = s.index('$')
    cap, unit = float(s[dollar_idx + 1:-2]), s[-2]
    if unit == 'B':
        cap *= 1000
    elif unit == 'T':
        cap *= 1000_000
    elif unit != 'M':
        logger.error(f'unsupported unit: {unit}')
        raise RuntimeError('unsupported unit')

    if s.startswith('Mega'):  # > 180B
        cap_enum = MarketCapType.MEGA
        if cap < 180_000: logger.debug(f'mega cap out of range: {cap}, {s}')
    elif s.startswith('Large'):  # 30B, 200B
        cap_enum = MarketCapType.LARGE
        if cap < 30_000 or cap > 200_000: logger.debug(f'large cap out of range: {cap}, {s}')
    elif s.startswith('Medium'):  # 5B, 35B
        cap_enum = MarketCapType.MID
        if cap < 5_000 or cap > 35_000: logger.debug(f'medium cap out of range: {cap}, {s}')
    elif s.startswith('Small'):  # 250M, 6B
        cap_enum = MarketCapType.SMALL
        if cap < 250 or cap > 6_000: logger.debug(f'small cap out of range: {cap}, {s}')
    elif s.startswith('Micro'):  # < 2B
        cap_enum = MarketCapType.MICRO
        if cap > 2_000: logger.debug(f'micro cap out of range: {cap}, {s}')
    else:
        logger.error(f'unsupported market cap type: {s}')
        raise RuntimeError('unsupported market cap type')
    return MarketCap(cap_enum, cap)


def construct_stock(r):
    """construct a Stack object from one row in csv"""
    stock = dict()
    for field in fields(Stock):
        name = field.name
        if name in COL_NAMES:
            stock[name] = r[COL_NAMES[name]]
    stock[MARKET_CAP_STR] = r[COL_NAMES[MARKET_CAP_STR]]
    (pe, volatility, cap_enum, cap, eps, rating, last, short, created, gain) = (
        'pe', 'volatility', 'cap_enum', 'cap', 'eps', 'rating', 'last', 'short', 'created', 'gain')
    stock[pe] = float(stock[pe])
    stock[volatility] = p2f(stock[volatility])
    market_cap = get_market_cap(stock[MARKET_CAP_STR])
    stock[cap_enum] = market_cap.category.value
    stock[cap] = market_cap.cap
    stock[eps] = d2f(stock[eps])
    stock[rating] = get_rating(stock[rating])
    stock[last] = d2f(stock[last])
    stock[short] = p2f(stock[short])
    del stock[MARKET_CAP_STR]
    stock[created] = datetime.today()
    stock[gain] = 0.0
    return Stock(**stock)


def save_watchlist_mongo():
    stocks = []
    for f in glob.glob(STOCK_WATCHLIST_PATH + '/*.csv'):
        df = pd.read_csv(f, header=2, index_col=False, skipfooter=30, engine='python')
        # print(df.shape)
        # print(df.head())
        # print(df.tail())
        # print(df['P/E ratio'][0])
        # print(type(df['P/E ratio'][0]))
        # print(df['Analyst ratings'][15])
        # print(df['Analyst ratings'][16])
        etf, na = 'ETF', '--'
        pe, industry, sector, volatility, eps, rating, short = (
            COL_NAMES['pe'], COL_NAMES['industry'], COL_NAMES['sector'], COL_NAMES['volatility'], COL_NAMES['eps'],
            COL_NAMES['rating'], COL_NAMES['short'])
        df.loc[df[pe] == na, pe] = 0.0  # fill 0.0 for N/A PE
        df.loc[df[industry] == na, industry] = etf  # N/A industry -> ETF
        df.loc[df[sector] == na, sector] = etf  # N/A sector -> ETF
        df.loc[df[volatility] == na, volatility] = '0.0%'
        df.loc[df[eps] == na, eps] = '$0'  # N/A eps -> 0
        df[rating] = df[rating].fillna('(0.0)')  # analyst rating not available
        df.loc[df[short] == na, short] = '0.0%'
        # print(df['Analyst ratings'][16])
        # print(df[df.isnull().any(axis=1)])  # row with at least one null
        if df.isnull().values.any():
            logger.error(df.loc[:, df.isnull().any()])
            raise RuntimeError('missing values')
        if df[df == '--'].notnull().values.any():
            logger.error(df.loc[:, df[df == '--'].any()])
            raise RuntimeError('-- value')
        # df[pe] = to_numeric(df[pe])
        # print(df.sort_values(by=[pe], ascending=True))
        print(df[pe])

        df.apply(lambda row: stocks.append(construct_stock(row)), axis=1)
    logger.info(f'total stocks in watchlist: {len(stocks)}')


if __name__ == '__main__':
    """testing"""
    save_watchlist_mongo()
