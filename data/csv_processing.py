import glob
import logging

import pandas as pd

from constants import STOCK_WATCHLIST_PATH

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def extract_column(file: str, col: str):
    """extra all rows for one column, comma delimited"""
    df = pd.read_csv(file, header=2, index_col=False, skipfooter=30, engine='python')
    # print(df.columns)
    return df[col].tolist()
    # print(df[col].tolist())
    # print(df.shape)
    # print(df.head())  # summary with first 5 rows


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
