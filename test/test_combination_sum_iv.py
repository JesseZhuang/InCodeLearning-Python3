from unittest import TestCase

from algorithm.dp.combination_sum_iv import Solution, Solution2


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_combination_sum_iv(self):
        cases = [
            ([1, 2, 3], 4, 7),
            ([9], 3, 0),
            ([1], 1, 1),
            ([1], 0, 1),
            ([1, 2], 4, 5),
            ([3, 1, 2, 4], 4, 8),
            ([1, 2, 3], 0, 1),
            ([5, 1, 8], 24, 982),
        ]
        for sol in self.solutions:
            for nums, target, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, nums=nums, t=target):
                    self.assertEqual(exp, sol.combinationSum4(list(nums), target))
