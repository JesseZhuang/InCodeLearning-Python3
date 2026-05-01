from unittest import TestCase

from algorithm.jzarray.count_fair_pairs import Solution


class TestCountFairPairs(TestCase):
    def test_count_fair_pairs(self):
        sol = Solution()
        self.assertEqual(6, sol.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6))
        self.assertEqual(1, sol.countFairPairs([1, 7, 9, 2, 5], 11, 11))
