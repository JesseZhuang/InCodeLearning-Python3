import unittest

from algorithm.heap.min_op_exceed_threshold_ii import Solution


class TestMinOperationsExceedThresholdII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        self.assertEqual(2, self.solution.minOperations([2, 11, 10, 1, 3], 10))

    def test_example_two(self):
        self.assertEqual(4, self.solution.minOperations([1, 1, 2, 4, 9], 20))

    def test_all_values_at_threshold(self):
        self.assertEqual(0, self.solution.minOperations([20, 20, 30], 20))

    def test_one_operation_reaches_threshold(self):
        self.assertEqual(1, self.solution.minOperations([5, 6], 16))

    def test_combined_value_exceeds_32_bit_range(self):
        self.assertEqual(
            1,
            self.solution.minOperations([999_999_999, 1_000_000_000], 1_000_000_000),
        )


if __name__ == "__main__":
    unittest.main()
