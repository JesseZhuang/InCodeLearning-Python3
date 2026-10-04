import unittest

from algorithm.binary_search.minimum_operations_to_make_all_array_elements_equal import Solution


class TestMinimumOperationsToMakeAllArrayElementsEqual(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_examples(self):
        for solution in self.solutions:
            self.assertEqual(solution.minOperations([3, 1, 6, 8], [1, 5]), [14, 10])
            self.assertEqual(solution.minOperations([2, 9, 6, 3], [10]), [20])

    def test_queries_below_at_and_above_values(self):
        nums = [3, 5, 5, 9]
        queries = [1, 3, 5, 9, 12]
        expected = [18, 10, 6, 14, 26]

        for solution in self.solutions:
            self.assertEqual(solution.minOperations(nums, queries), expected)

    def test_large_total_uses_wide_arithmetic(self):
        nums = [1] * 100_000

        for solution in self.solutions:
            self.assertEqual(solution.minOperations(nums, [1_000_000_000]), [99_999_999_900_000])


if __name__ == "__main__":
    unittest.main()
