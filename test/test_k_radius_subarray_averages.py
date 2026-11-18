import unittest

from algorithm.sliding.k_radius_subarray_averages import Solution


class KRadiusSubarrayAveragesTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_example(self):
        self.assertEqual(
            [-1, -1, -1, 5, 4, 4, -1, -1, -1],
            self.solution.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3),
        )

    def test_zero_radius_returns_each_value(self):
        self.assertEqual([4, -2, 0], self.solution.getAverages([4, -2, 0], 0))

    def test_window_larger_than_array_has_no_valid_center(self):
        self.assertEqual([-1, -1], self.solution.getAverages([8, 5], 1))

    def test_exactly_one_full_window(self):
        self.assertEqual([-1, 2, -1], self.solution.getAverages([1, 2, 3], 1))

    def test_first_and_last_valid_centers(self):
        self.assertEqual(
            [-1, 1, 2, 2, -1],
            self.solution.getAverages([4, -2, 2, 6, -1], 1),
        )

    def test_negative_average_truncates_toward_zero(self):
        self.assertEqual([-1, -2, -1], self.solution.getAverages([-4, -2, -1], 1))

    def test_prefix_sum_variant_matches_edge_cases(self):
        cases = [
            ([7, 4, 3, 9, 1, 8, 5, 2, 6], 3, [-1, -1, -1, 5, 4, 4, -1, -1, -1]),
            ([4, -2, 0], 0, [4, -2, 0]),
            ([8, 5], 1, [-1, -1]),
            ([1, 2, 3], 1, [-1, 2, -1]),
            ([4, -2, 2, 6, -1], 1, [-1, 1, 2, 2, -1]),
            ([-4, -2, -1], 1, [-1, -2, -1]),
        ]
        for nums, k, expected in cases:
            with self.subTest(nums=nums, k=k):
                self.assertEqual(expected, self.solution.getAveragesByPrefixSum(nums, k))


if __name__ == "__main__":
    unittest.main()
