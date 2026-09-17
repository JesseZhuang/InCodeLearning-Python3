import unittest

from algorithm.hash.binary_subarrays_with_sum import Solution, Solution2


class TestBinarySubarraysWithSum(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.numSubarraysWithSum([1, 0, 1, 0, 1], 2), 4)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.numSubarraysWithSum([0, 0, 0, 0, 0], 0), 15)

    def test_single_one_goal_one(self):
        for sol in self.solutions:
            self.assertEqual(sol.numSubarraysWithSum([1], 1), 1)

    def test_single_zero_goal_zero(self):
        for sol in self.solutions:
            self.assertEqual(sol.numSubarraysWithSum([0], 0), 1)

    def test_single_one_goal_zero(self):
        for sol in self.solutions:
            self.assertEqual(sol.numSubarraysWithSum([1], 0), 0)

    def test_all_ones(self):
        for sol in self.solutions:
            self.assertEqual(sol.numSubarraysWithSum([1, 1, 1, 1], 2), 3)

    def test_goal_equals_length(self):
        for sol in self.solutions:
            self.assertEqual(sol.numSubarraysWithSum([1, 1, 1], 3), 1)

    def test_goal_zero_with_mixed(self):
        for sol in self.solutions:
            self.assertEqual(sol.numSubarraysWithSum([1, 0, 0, 1], 0), 3)

    def test_leading_trailing_zeros(self):
        for sol in self.solutions:
            self.assertEqual(sol.numSubarraysWithSum([0, 0, 1, 0, 0], 1), 9)

    def test_no_valid_subarray(self):
        for sol in self.solutions:
            self.assertEqual(sol.numSubarraysWithSum([0, 0, 0], 1), 0)

    def test_large_goal(self):
        for sol in self.solutions:
            self.assertEqual(sol.numSubarraysWithSum([1, 0, 1], 5), 0)


if __name__ == "__main__":
    unittest.main()
