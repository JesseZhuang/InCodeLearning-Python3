import unittest
from itertools import combinations, product

from algorithm.jzarray.minimum_operations_to_make_array_increasing import Solution


class TestMinimumOperationsToMakeArrayIncreasing(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def assert_operations(self, nums, expected):
        for solution in self.solutions:
            with self.subTest(nums=nums):
                original = nums.copy()
                self.assertEqual(expected, solution.minOperations(nums))
                self.assertEqual(original, nums)

    def test_example_equal_values(self):
        self.assert_operations([1, 1, 1], 3)

    def test_example_mixed_values(self):
        self.assert_operations([1, 5, 2, 4, 1], 14)

    def test_example_single_element(self):
        self.assert_operations([8], 0)

    def test_single_element_boundaries(self):
        self.assert_operations([1], 0)
        self.assert_operations([10_000], 0)

    def test_already_strictly_increasing(self):
        self.assert_operations([1, 2, 3, 4, 5], 0)

    def test_increasing_with_large_gaps(self):
        self.assert_operations([1, 10, 10_000], 0)

    def test_equal_adjacent_values_need_increment(self):
        self.assert_operations([2, 2], 1)

    def test_descending_values(self):
        self.assert_operations([5, 4, 3, 2, 1], 20)

    def test_adjustments_carry_forward(self):
        self.assert_operations([2, 1, 1, 1], 9)

    def test_larger_value_resets_threshold(self):
        self.assert_operations([3, 1, 10, 1], 13)

    def test_exact_threshold_needs_no_additional_increment(self):
        self.assert_operations([3, 3, 5], 1)

    def test_adjusted_values_can_exceed_input_upper_bound(self):
        self.assert_operations([10_000, 10_000], 1)

    def test_maximum_length_equal_values(self):
        self.assert_operations([1] * 5_000, 12_497_500)
        self.assert_operations([10_000] * 5_000, 12_497_500)

    def test_maximum_operations_within_constraints(self):
        self.assert_operations([10_000] + [1] * 4_999, 62_482_501)

    def test_repeated_calls_do_not_share_state(self):
        self.assert_operations([1, 1, 1], 3)
        self.assert_operations([1, 2, 3], 0)
        self.assert_operations([1, 1, 1], 3)

    def test_exhaustive_small_inputs_against_sequence_enumeration(self):
        for length in range(1, 5):
            for values in product(range(1, 4), repeat=length):
                expected = min(
                    sum(adjusted - original for adjusted, original in zip(candidate, values))
                    for candidate in combinations(range(1, max(values) + length + 1), length)
                    if all(adjusted >= original for adjusted, original in zip(candidate, values))
                )
                self.assert_operations(list(values), expected)


if __name__ == "__main__":
    unittest.main()
