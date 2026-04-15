import unittest

from algorithm.hash.subarray_sum_equals_k import Solution, Solution2


class TestSubarraySumEqualsK(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, nums, k, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.subarraySum(nums, k))

    def test_example1(self):
        self.verify([1, 1, 1], 2, 2)

    def test_example2(self):
        self.verify([1, 2, 3], 3, 2)

    def test_single_match(self):
        self.verify([1], 1, 1)

    def test_single_no_match(self):
        self.verify([1], 0, 0)

    def test_negative_numbers(self):
        self.verify([-1, -1, 1], 0, 1)

    def test_all_zeros(self):
        self.verify([0, 0, 0], 0, 6)

    def test_k_negative(self):
        self.verify([1, -1, 0], -1, 2)

    def test_prefix_sum_zero(self):
        self.verify([1, -1, 1, -1], 0, 4)

    def test_large_k(self):
        self.verify([1, 2, 3, 4, 5], 15, 1)

    def test_no_match(self):
        self.verify([1, 2, 3], 7, 0)
