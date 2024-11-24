import glob
import logging
from dataclasses import fields
from datetime import datetime

import pandas as pd

from constants import STOCK_WATCHLIST_PATH, COL_NAMES, MARKET_CAP_STR
from data.model.stock import Stock, MarketCapType, MarketCap

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


def extract_col_to_list_glob(dir: str):
    """extract one column from multiple csv files"""
    res = set()
    for f in glob.glob(dir + '/*.csv'):
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
    """str to market cap, Mega Cap ($3.40T) -> (MEGA(4),3.4)"""
    dollar_idx = s.index('$')
    cap, unit = float(s[dollar_idx + 1:-2]), s[-2]
    if unit == 'B':
        cap *= 1000
    elif unit == 'T':
        cap *= 1000_000
    elif unit != 'M':
        logger.error(f'unsupported unit: {unit}')
        raise RuntimeError('unsupported unit')

    if s.startswith('Mega'):
        cap_enum = MarketCapType.MEGA
        if cap < 200_000: logger.debug('mega cap out of range: {cap}, {s}')
    elif s.startswith('Large'):
        cap_enum = MarketCapType.LARGE
        if cap < 30_000 or cap > 200_000: logger.debug('large cap out of range: {cap}, {s}')
    elif s.startswith('Medium'):
        cap_enum = MarketCapType.MID
        if cap < 5_000 or cap > 30_000: logger.debug('medium cap out of range: {cap}, {s}')
    elif s.startswith('Small'):
        cap_enum = MarketCapType.SMALL
        if cap < 250 or cap > 5_000: logger.debug('small cap out of range: {cap}, {s}')
    elif s.startswith('Micro'):
        cap_enum = MarketCapType.MICRO
        logger.warning(f'be careful with micro cap stocks: {s}')
        if cap > 250: logger.debug(f'micro cap out of range: {cap}, {s}')
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
    (pe, volatility, cap_enum, cap, eps, rating, last, short, created) = (
        'pe', 'volatility', 'cap_enum', 'cap', 'eps', 'rating', 'last', 'short', 'created')
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
        pe, industry, sector, eps, rating, short = (
            COL_NAMES['pe'], COL_NAMES['industry'], COL_NAMES['sector'], COL_NAMES['eps'],
            COL_NAMES['rating'], COL_NAMES['short'])
        df.loc[df[pe] == na, pe] = 0.0  # fill 0.0 for N/A PE
        df.loc[df[industry] == na, industry] = etf  # N/A industry -> ETF
        df.loc[df[sector] == na, sector] = etf  # N/A sector -> ETF
        df.loc[df[eps] == na, eps] = '$0'  # N/A eps -> 0
        df[rating] = df[rating].fillna('(0.0)')  # analyst rating not available
        df.loc[df[short] == na, short] = '0.0%'
        # print(df['Analyst ratings'][16])

        df.apply(lambda row: stocks.append(construct_stock(row)), axis=1)


if __name__ == '__main__':
    """testing"""
    print(save_watchlist_mongo())
