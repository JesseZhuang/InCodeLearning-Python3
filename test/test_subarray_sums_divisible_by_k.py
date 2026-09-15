import unittest

from algorithm.hash.subarray_sums_divisible_by_k import Solution, Solution2


class TestSubarraySumsDivisibleByK(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, nums, k, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.subarraysDivByK(nums, k))

    def test_example1(self):
        self.verify([4, 5, 0, -2, -3, 1], 5, 7)

    def test_example2(self):
        self.verify([5], 9, 0)

    def test_all_divisible(self):
        self.verify([5, 10, 15], 5, 6)

    def test_single_zero(self):
        self.verify([0], 1, 1)

    def test_negative_numbers(self):
        self.verify([-1, 2, 9], 2, 2)

    def test_all_zeros(self):
        self.verify([0, 0, 0], 3, 6)

    def test_large_k(self):
        self.verify([1, 2, 3], 100, 0)

    def test_k_equals_1(self):
        self.verify([1, 2, 3], 1, 6)

    def test_negative_prefix(self):
        self.verify([-5, 1, 2, -3, 4], 5, 3)

    def test_single_element_divisible(self):
        self.verify([6], 3, 1)
