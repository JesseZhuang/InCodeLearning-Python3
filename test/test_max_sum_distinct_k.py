from unittest import TestCase

from algorithm.jzarray.max_sum_distinct_k import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_maximum_subarray_sum(self):
        cases = [
            ([1, 5, 4, 2, 9, 9, 9], 3, 15),
            ([4, 4, 4], 3, 0),
        ]
        for sol in self.solutions:
            for nums, k, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, nums=nums, k=k):
                    self.assertEqual(sol.maximumSubarraySum(list(nums), k), exp)
