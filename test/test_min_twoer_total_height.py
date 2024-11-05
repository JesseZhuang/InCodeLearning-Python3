import unittest

from algorithm.array.max_tower_total_height import Solution2


class TestMinTowerTotalHeight(unittest.TestCase):

    def test_solution(self):
        test_cases = [
            [[2, 3, 4, 3], 10],
            [[15, 10], 25],
            [[2, 2, 1], -1],
            [[6, 6, 6, 3, 7, 2, 6, 5], -1]
        ]
        tbt = Solution2()
        for l, exp in test_cases:
            with self.subTest(l):
                self.assertEqual(exp, tbt.maximumTotalSum(l))
