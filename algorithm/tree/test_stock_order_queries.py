'''unit test stock order queries'''
import unittest

# use vs code python test explorer plugin
from algorithm.tree.stock_order_queries import StockOrder

# pylint: disable=invalid-name


class StockOrderTest(unittest.TestCase):
    '''unit test the class'''

    def setUp(self) -> None:
        self.orders = []
        for x in range(10):
            self.orders.append(StockOrder(x, 10, 1.01, True, x, x + 5))
        self.queries = [3, 6]

    def test_auto_generated_constructor(self):
        '''constructor and string representation'''
        order = StockOrder(2, 10, 1.31, True, 120, 10000)
        print(order)
        self.assertEqual(2, order.order_token)

    def test_bf(self):
        '''test brute forece method'''
        result = StockOrder.num_shares_queries_bf(self.orders, self.queries)
        self.assertEqual([40, 50], result)  # [0,3] orders for 3 query, [2,6] for the 6 query
