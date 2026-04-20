from unittest import TestCase

from algorithm.dp.longest_increasing_subsequence import Solution, Solution2


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_length_of_lis(self):
        cases = [
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([0, 1, 0, 3, 2, 3], 4),
            ([7, 7, 7, 7, 7, 7, 7], 1),
            ([1], 1),
            ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
            ([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12], 6),
            ([10, 22, 9, 33, 21, 50, 41, 60], 5),
        ]
        for sol in self.solutions:
            for nums, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, nums=nums, exp=exp):
                    self.assertEqual(sol.lengthOfLIS(nums), exp)
