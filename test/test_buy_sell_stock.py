import unittest

from algorithm.dp.buy_sell_stock import Solution, Solution2


class TestBuySellStock(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(5, s.maxProfit([7, 1, 5, 3, 6, 4]))

    def test_example2_decreasing(self):
        for s in self.solutions:
            self.assertEqual(0, s.maxProfit([7, 6, 4, 3, 1]))

    def test_single_element(self):
        for s in self.solutions:
            self.assertEqual(0, s.maxProfit([5]))

    def test_two_increasing(self):
        for s in self.solutions:
            self.assertEqual(1, s.maxProfit([1, 2]))

    def test_two_decreasing(self):
        for s in self.solutions:
            self.assertEqual(0, s.maxProfit([2, 1]))

    def test_all_same(self):
        for s in self.solutions:
            self.assertEqual(0, s.maxProfit([3, 3, 3, 3]))

    def test_profit_at_end(self):
        for s in self.solutions:
            self.assertEqual(8, s.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))

    def test_min_at_start_max_at_end(self):
        for s in self.solutions:
            self.assertEqual(10000, s.maxProfit([0, 10000]))

    def test_large_dip_then_rise(self):
        for s in self.solutions:
            self.assertEqual(8, s.maxProfit([3, 8, 1, 9, 2]))

    def test_alternating(self):
        for s in self.solutions:
            self.assertEqual(1, s.maxProfit([1, 2, 1, 2, 1, 2]))


if __name__ == '__main__':
    unittest.main()
