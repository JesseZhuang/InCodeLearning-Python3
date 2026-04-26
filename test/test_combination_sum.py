from unittest import TestCase

from algorithm.jzarray.combination_sum import Solution, Solution2


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_combination_sum(self):
        cases = [
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
            ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
            ([2], 1, []),
            ([1], 1, [[1]]),
            ([1], 2, [[1, 1]]),
            ([1, 2], 4, [[1, 1, 1, 1], [1, 1, 2], [2, 2]]),
        ]
        for sol in self.solutions:
            for candidates, target, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, c=candidates, t=target):
                    result = sol.combinationSum(list(candidates), target)
                    self.assertEqual(
                        sorted([sorted(x) for x in result]),
                        sorted([sorted(x) for x in exp]),
                    )
