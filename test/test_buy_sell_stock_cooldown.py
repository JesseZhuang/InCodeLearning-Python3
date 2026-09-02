import unittest

from algorithm.dp.buy_sell_stock_cooldown import Solution, Solution2


class TestBuySellStockCooldown(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(3, s.maxProfit([1, 2, 3, 0, 2]))

    def test_example2_single(self):
        for s in self.solutions:
            self.assertEqual(0, s.maxProfit([1]))

    def test_two_increasing(self):
        for s in self.solutions:
            self.assertEqual(1, s.maxProfit([1, 2]))

    def test_two_decreasing(self):
        for s in self.solutions:
            self.assertEqual(0, s.maxProfit([2, 1]))

    def test_all_decreasing(self):
        for s in self.solutions:
            self.assertEqual(0, s.maxProfit([5, 4, 3, 2, 1]))

    def test_all_same(self):
        for s in self.solutions:
            self.assertEqual(0, s.maxProfit([3, 3, 3, 3]))

    def test_cooldown_matters(self):
        """Without cooldown profit=4 (buy1 sell2 buy3 sell4), with cooldown=3."""
        for s in self.solutions:
            self.assertEqual(3, s.maxProfit([1, 2, 3, 4]))

    def test_multiple_transactions(self):
        for s in self.solutions:
            self.assertEqual(6, s.maxProfit([1, 2, 3, 0, 2, 4, 0, 3]))

    def test_long_cooldown_benefit(self):
        for s in self.solutions:
            self.assertEqual(6, s.maxProfit([1, 4, 2, 7]))

    def test_alternating_prices(self):
        for s in self.solutions:
            self.assertEqual(2, s.maxProfit([1, 3, 1, 3, 1]))

    def test_large_gap(self):
        for s in self.solutions:
            self.assertEqual(1000, s.maxProfit([0, 1000]))

    def test_three_elements_peak_middle(self):
        for s in self.solutions:
            self.assertEqual(4, s.maxProfit([1, 5, 0]))


if __name__ == '__main__':
    unittest.main()
