import unittest

from algorithm.jzarray.sum_of_unique_elements import Solution


class TestSumOfUniqueElements(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_element_is_unique(self):
        self.assertEqual(self.solution.sumOfUnique([5]), 5)
        self.assertEqual(self.solution.sumOfUniqueBySorting([5]), 5)

    def test_all_distinct_values_are_summed(self):
        self.assertEqual(self.solution.sumOfUnique([1, 2, 3]), 6)
        self.assertEqual(self.solution.sumOfUniqueBySorting([1, 2, 3]), 6)

    def test_repeated_values_are_excluded(self):
        nums = [1, 2, 2, 3, 3, 3]
        self.assertEqual(self.solution.sumOfUnique(nums), 1)
        self.assertEqual(self.solution.sumOfUniqueBySorting(nums), 1)

    def test_values_repeated_more_than_twice_are_excluded(self):
        nums = [6, 6, 6, 7, 8, 8]
        self.assertEqual(self.solution.sumOfUnique(nums), 7)
        self.assertEqual(self.solution.sumOfUniqueBySorting(nums), 7)

    def test_sorting_approach_does_not_mutate_input(self):
        nums = [4, 2, 4, 3]
        original = nums[:]
        self.assertEqual(self.solution.sumOfUniqueBySorting(nums), 5)
        self.assertEqual(nums, original)


if __name__ == "__main__":
    unittest.main()
