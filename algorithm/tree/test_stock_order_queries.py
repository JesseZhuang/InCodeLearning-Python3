'''unit test stock order queries'''
import unittest

from algorithm.tree.stock_order_queries import StockOrder


class StockOrderTest(unittest.TestCase):
    '''unit test the class'''
    def test_auto_generated_constructor(self):
        '''constructor and string representation'''
        order = StockOrder(2, 10, 1.31, True, 120, 10000)
        print(order)
        self.assertEqual(2, order.order_token)
