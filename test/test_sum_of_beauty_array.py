import unittest

from algorithm.jzarray.sum_of_beauty_array import Solution


class TestSumOfBeautyArray(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_global_beauty_is_two(self):
        self.assertEqual(2, self.solution.sumOfBeauties([1, 2, 3]))

    def test_global_beauty_takes_precedence_over_local_beauty(self):
        self.assertEqual(4, self.solution.sumOfBeauties([1, 3, 4, 5]))

    def test_local_beauty_is_one_when_global_left_condition_fails(self):
        self.assertEqual(1, self.solution.sumOfBeauties([4, 2, 3, 5]))

    def test_local_beauty_is_one_when_global_right_condition_fails(self):
        self.assertEqual(1, self.solution.sumOfBeauties([1, 2, 3, 2]))

    def test_no_beauty_for_descending_values(self):
        self.assertEqual(0, self.solution.sumOfBeauties([3, 2, 1]))

    def test_comparisons_are_strict(self):
        self.assertEqual(0, self.solution.sumOfBeauties([1, 2, 2, 3]))

    def test_large_increasing_input(self):
        nums = list(range(1, 100_001))
        self.assertEqual(2 * (len(nums) - 2), self.solution.sumOfBeauties(nums))
