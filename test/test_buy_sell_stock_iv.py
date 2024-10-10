import unittest

from algorithm.dp.buy_sell_stock_iv import Solution


class TestBuySellStock(unittest.TestCase):

    def setUp(self):
        self.tbt = Solution()

    def test_buy_sell_stock(self):
        """
        prices must be outer loop, see buy sell stock iii, update b1,s1 then b2,s2
        for this test case, if k is outer loop, 6-2 will be considered twice and max profit is 8 instead of 7
        """
        self.assertEqual(7, self.tbt.maxProfit(2, [3, 2, 6, 5, 0, 3]))
