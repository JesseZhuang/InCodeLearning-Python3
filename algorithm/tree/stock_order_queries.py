'''stock oder queries'''

from bisect import bisect_right
from dataclasses import dataclass


@dataclass
class StockOrder:
    '''stock trading order'''
    order_token: int  # order id
    shares: int  # number of shares
    price: float
    side: bool  # false = sell, true = buy
    # order is live [created_at, cancelled_or_executed_at), can assume cancelled or executed in full
    created_at: int  # timestamp, milli since midnight
    cancelled_or_executed_at: int

    @classmethod
    def num_shares_queries_bf(cls, orders: list['StockOrder'], queries: list[int]) -> list[int]:
        '''
        orders: list of orders over a day, N orders
        queries: each query_time is a timestamp, M queries
        Answer to the query is total number of outstanding shares at the query time.
        Outstanding shares are agreegated, e.g., open orders to buy 10 and sell 10 aggregate to 20 shares live.
        return answers, one for each query, in the same order as respective queries
        naive implementation: O(N*M) time, O(M) space
        '''
        result = [0] * len(queries)
        for order in orders:
            for i, query in enumerate(queries):
                if query < order.cancelled_or_executed_at and query >= order.created_at:
                    result[i] += order.shares
        return result

    @classmethod
    def num_shares_queries_bs(cls, orders: list['StockOrder'], queries: list[int]) -> list[int]:
        '''
        binary search, O((M+N)LgN) time, O(M) space. continuous memory access
        alternatively, binary search queries, O((M+N)LgM) time. random memory access
        note bisect functions key argument was added since 3.10
        '''
        result = [0] * len(queries)
        orders_sortby_create = sorted(orders, key=lambda order: order.created_at)  # O(NlgN)
        for i, query in enumerate(queries):  # (MLgN) time
            filter_start = bisect_right(orders_sortby_create, query, key=lambda order: order.created_at)
            # assume size K (K <= N) after filtering, O(KLgK) time
            orders_sortby_end = sorted(orders_sortby_create[:filter_start],
                                       key=lambda order: order.cancelled_or_executed_at)
            filter_end = bisect_right(orders_sortby_end, query, key=lambda order: order.cancelled_or_executed_at)
            orders = orders_sortby_end[filter_end:]
            for order in orders:
                result[i] += order.shares
        return result
