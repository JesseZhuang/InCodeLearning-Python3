"""test LeetCode 312 Burst Balloons"""
import unittest

from algorithm.dp.burst_balloons import Solution, Solution2


class TestBurstBalloons(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(167, sol.maxCoins([3, 1, 5, 8]))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(10, sol.maxCoins([1, 5]))

    def test_single_balloon(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.maxCoins([3]))

    def test_two_same(self):
        for sol in self.solutions:
            self.assertEqual(6, sol.maxCoins([2, 2]))

    def test_ascending(self):
        for sol in self.solutions:
            self.assertEqual(40, sol.maxCoins([1, 2, 3, 4]))

    def test_descending(self):
        for sol in self.solutions:
            self.assertEqual(40, sol.maxCoins([4, 3, 2, 1]))

    def test_large_values(self):
        for sol in self.solutions:
            self.assertEqual(balance_check([100, 100, 100]), sol.maxCoins([100, 100, 100]))

    def test_single_one(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.maxCoins([1]))


def balance_check(nums):
    """Brute force for small inputs to verify."""
    if not nums:
        return 0
    max_coins = 0
    for i in range(len(nums)):
        left = nums[i - 1] if i > 0 else 1
        right = nums[i + 1] if i < len(nums) - 1 else 1
        coins = left * nums[i] * right + balance_check(nums[:i] + nums[i + 1:])
        max_coins = max(max_coins, coins)
    return max_coins


if __name__ == '__main__':
    unittest.main()
