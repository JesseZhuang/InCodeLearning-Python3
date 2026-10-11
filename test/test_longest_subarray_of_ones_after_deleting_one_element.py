import unittest

from algorithm.sliding.longest_subarray_of_ones_after_deleting_one_element import (
    Solution,
    Solution2,
)


class TestLongestSubarrayOfOnesAfterDeletingOneElement(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_examples(self):
        cases = [
            ([1, 1, 0, 1], 3),
            ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
        ]
        for nums, expected in cases:
            for solution in self.solutions:
                with self.subTest(nums=nums, solution=type(solution).__name__):
                    self.assertEqual(expected, solution.longestSubarray(nums))

    def test_deletes_one_even_when_all_values_are_one(self):
        for solution in self.solutions:
            self.assertEqual(2, solution.longestSubarray([1, 1, 1]))

    def test_all_zeros(self):
        for solution in self.solutions:
            self.assertEqual(0, solution.longestSubarray([0, 0, 0]))

    def test_single_element(self):
        for solution in self.solutions:
            self.assertEqual(0, solution.longestSubarray([1]))
            self.assertEqual(0, solution.longestSubarray([0]))

    def test_deletes_the_zero_between_long_runs(self):
        for solution in self.solutions:
            self.assertEqual(5, solution.longestSubarray([1, 0, 1, 1, 1, 0, 1, 1]))


if __name__ == "__main__":
    unittest.main()
