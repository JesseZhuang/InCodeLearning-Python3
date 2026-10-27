"""Tests for LeetCode 2215, Find the Difference of Two Arrays."""
import unittest

from algorithm.hash.find_the_difference_of_two_arrays import Solution


class TestFindTheDifferenceOfTwoArrays(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_distinct_values_on_both_sides(self):
        self.check_difference([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]])

    def test_duplicates_only_appear_once(self):
        self.check_difference([1, 2, 3, 3], [1, 1, 2, 2], [[3], []])

    def test_equal_arrays_have_no_difference(self):
        self.check_difference([4, 4, -2], [-2, 4, 4], [[], []])

    def test_disjoint_singletons_and_bounds(self):
        self.check_difference([-1000], [1000], [[-1000], [1000]])

    def test_only_second_array_has_distinct_values(self):
        self.check_difference([7], [7, 8, 8], [[], [8]])

    def test_only_first_array_has_distinct_values(self):
        self.check_difference([7, -8, -8], [7], [[-8], []])

    def test_maximum_input_length(self):
        self.check_difference(list(range(1000)), list(range(1, 1001)), [[0], [1000]])

    def check_difference(self, nums1, nums2, expected):
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__, nums1=nums1[:4]):
                result = solution.findDifference(nums1, nums2)
                self.assertEqual(len(result), 2)
                self.assertEqual([sorted(values) for values in result],
                                 [sorted(values) for values in expected])


if __name__ == '__main__':
    unittest.main()
