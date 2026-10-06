import unittest
from functools import lru_cache
from itertools import product

from algorithm.heap.maximal_score_after_k_operations import Solution


class TestMaximalScoreAfterKOperations(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def assert_score(self, nums, operations, expected):
        for solution in self.solutions:
            with self.subTest(nums=nums, operations=operations):
                original = nums.copy()
                self.assertEqual(expected, solution.maxKelements(nums, operations))
                self.assertEqual(original, nums)

    def test_example_equal_values(self):
        self.assert_score([10, 10, 10, 10, 10], 5, 50)

    def test_example_repeated_selection(self):
        self.assert_score([1, 10, 3, 3, 3], 3, 17)

    def test_one_operation_selects_largest(self):
        self.assert_score([2, 9, 4], 1, 9)

    def test_rounding_all_remainders(self):
        for value, expected in [(3, 5), (4, 7), (5, 8), (6, 9)]:
            self.assert_score([value], 3, expected)

    def test_heap_order_changes_after_replacement(self):
        self.assert_score([9, 8], 4, 23)

    def test_equal_values_then_fixed_point(self):
        self.assert_score([2, 2], 5, 7)

    def test_all_ones(self):
        self.assert_score([1, 1, 1], 8, 8)

    def test_single_element_maximum_operations(self):
        self.assert_score([1], 100_000, 100_000)

    def test_large_value_rounding(self):
        self.assert_score([1_000_000_000], 3, 1_444_444_446)

    def test_score_exceeds_signed_32_bit(self):
        self.assert_score([1_000_000_000] * 3, 3, 3_000_000_000)

    def test_maximum_constraints(self):
        self.assert_score([1_000_000_000] * 100_000, 100_000, 100_000_000_000_000)

    def test_exhaustive_small_inputs_against_optimal_search(self):
        @lru_cache(maxsize=None)
        def optimal_score(values, remaining):
            if remaining == 0:
                return 0
            scores = []
            for index, value in enumerate(values):
                quotient, remainder = divmod(value, 3)
                updated = list(values)
                updated[index] = quotient + bool(remainder)
                scores.append(value + optimal_score(tuple(updated), remaining - 1))
            return max(scores)

        for length in range(1, 4):
            for values in product(range(1, 5), repeat=length):
                for operations in range(1, 5):
                    self.assert_score(
                        list(values), operations, optimal_score(values, operations)
                    )


if __name__ == "__main__":
    unittest.main()
