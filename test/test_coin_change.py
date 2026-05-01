"""test LeetCode 322 Coin Change"""
import unittest

from algorithm.dp.coin_change import Solution, Solution2


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.coinChange([1, 2, 5], 11))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(-1, sol.coinChange([2], 3))

    def test_zero_amount(self):
        for sol in self.solutions:
            self.assertEqual(0, sol.coinChange([1], 0))

    def test_single_coin_exact(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.coinChange([3], 6))

    def test_single_coin_impossible(self):
        for sol in self.solutions:
            self.assertEqual(-1, sol.coinChange([3], 7))

    def test_large_coins(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.coinChange([1, 5, 10, 25], 30))

    def test_greedy_fails(self):
        """Greedy picks 6+1+1+1 = 4 coins, but optimal is 5+5+5 = 3 coins."""
        for sol in self.solutions:
            self.assertEqual(3, sol.coinChange([1, 5, 6], 15))

    def test_amount_one(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.coinChange([1, 2, 5], 1))

    def test_all_coins_larger(self):
        for sol in self.solutions:
            self.assertEqual(-1, sol.coinChange([5, 10], 3))


if __name__ == '__main__':
    unittest.main()
