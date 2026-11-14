import unittest

from algorithm.sliding.minimum_operations_to_reduce_x_to_zero import Solution, Solution2


class MinimumOperationsToReduceXToZeroTest(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def assert_all_solutions(self, nums, x, expected):
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__, nums=nums, x=x):
                self.assertEqual(expected, solution.minOperations(nums, x))

    def test_standard_example_keeps_longest_complement(self):
        self.assert_all_solutions([1, 1, 4, 2, 3], 5, 2)

    def test_removing_both_ends_keeps_longest_interior_complement(self):
        self.assert_all_solutions([3, 2, 20, 1, 1, 3], 10, 5)

    def test_x_greater_than_total_is_impossible(self):
        self.assert_all_solutions([1, 2, 3], 7, -1)

    def test_missing_contiguous_complement_is_impossible(self):
        self.assert_all_solutions([5, 6, 7, 8, 9], 4, -1)

    def test_x_equal_to_total_removes_every_element(self):
        self.assert_all_solutions([1, 2, 3], 6, 3)

    def test_zero_x_removes_nothing(self):
        self.assert_all_solutions([1, 2, 3], 0, 0)

    def test_positive_target_without_a_contiguous_complement_is_impossible(self):
        self.assert_all_solutions([1, 2, 3], 2, -1)

    def test_single_element_is_removed(self):
        self.assert_all_solutions([1], 1, 1)


if __name__ == "__main__":
    unittest.main()
