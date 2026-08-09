import unittest

from algorithm.sliding.longest_subarray_abs_diff_limit import Solution, Solution2


class TestLongestSubarrayAbsDiffLimit(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.longestSubarray([8, 2, 4, 7], 4))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(4, sol.longestSubarray([10, 1, 2, 4, 7, 2], 5))

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))

    def test_single_element(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.longestSubarray([5], 0))

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.longestSubarray([3, 3, 3, 3, 3], 0))

    def test_limit_zero_alternating(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.longestSubarray([1, 2, 1, 2, 1], 0))

    def test_large_limit(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.longestSubarray([1, 5, 9, 2, 7], 100))

    def test_decreasing(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.longestSubarray([9, 8, 7, 6, 5], 2))

    def test_increasing(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.longestSubarray([1, 2, 3, 4, 5], 2))

    def test_two_elements_within_limit(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.longestSubarray([1, 3], 2))

    def test_two_elements_exceed_limit(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.longestSubarray([1, 4], 2))


if __name__ == '__main__':
    unittest.main()
