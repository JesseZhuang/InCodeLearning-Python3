import unittest

from algorithm.bit.longest_subarray_with_maximum_bitwise_and import Solution


class TestLongestSubarrayWithMaximumBitwiseAnd(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_examples(self):
        cases = [
            ([1, 2, 3, 3, 2, 2], 2),
            ([1, 2, 3, 4], 1),
        ]
        for nums, expected in cases:
            for solution in self.solutions:
                with self.subTest(nums=nums):
                    self.assertEqual(expected, solution.longestSubarray(nums))

    def test_single_element_and_all_equal(self):
        for solution in self.solutions:
            self.assertEqual(1, solution.longestSubarray([1]))
            self.assertEqual(4, solution.longestSubarray([7, 7, 7, 7]))

    def test_longest_run_is_after_a_smaller_value(self):
        for solution in self.solutions:
            self.assertEqual(3, solution.longestSubarray([5, 5, 3, 5, 5, 5]))

    def test_later_higher_maximum_discards_previous_best(self):
        for solution in self.solutions:
            self.assertEqual(2, solution.longestSubarray([4, 4, 4, 2, 6, 6, 3]))

    def test_shorter_later_run_does_not_replace_best(self):
        for solution in self.solutions:
            self.assertEqual(3, solution.longestSubarray([9, 9, 9, 1, 9, 9]))

    def test_constraint_boundaries(self):
        for solution in self.solutions:
            self.assertEqual(2, solution.longestSubarray([1, 1_000_000, 1_000_000, 1]))
            self.assertEqual(99_999, solution.longestSubarray([1] + [1_000_000] * 99_999))


if __name__ == "__main__":
    unittest.main()
