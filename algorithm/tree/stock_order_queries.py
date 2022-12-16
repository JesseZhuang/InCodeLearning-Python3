'''stock oder queries'''

from dataclasses import dataclass


@dataclass
class StockOrder:
    '''stock trading order'''
    order_token: int  # order id
    shares: int  # number of shares
    price: float
    side: bool  # false = sell, true = buy
    # order is live [created_at, cancelled_or_executed_at)
    created_at: int  # timestamp, milli since midnight
    cancelled_or_executed_at: int

    @classmethod
    def num_shares_queries(cls, orders: list['StockOrder'], queries: list[int]) -> list[int]:
        '''
        orders: list of orders over a day
        queries: each query_time is a timestamp
        Answer to the query is total number of outstanding shares at the query time.
        Outstanding shares are agreegated, e.g., open orders to buy 10 and sell 10 aggregate to 20 shares live.
        return answers, one for each query, in the same order as respective queries
        '''
        return []
