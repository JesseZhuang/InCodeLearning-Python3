from unittest import TestCase

from algorithm.jzarray.partition_array_into_three_parts_with_equal_sum import Solution


class TestPartitionArrayIntoThreePartsWithEqualSum(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_can_split_official_examples(self):
        cases = [
            ([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], True),
            ([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], False),
            ([3, 3, 6, 5, -2, 2, 5, 1, -9, 4], True),
        ]
        for arr, expected in cases:
            for solution in self.solutions:
                with self.subTest(arr=arr):
                    self.assertEqual(solution.canThreePartsEqualSum(arr), expected)

    def test_all_zero_values_make_three_nonempty_parts(self):
        for solution in self.solutions:
            self.assertTrue(solution.canThreePartsEqualSum([0, 0, 0, 0]))

    def test_nondivisible_total_cannot_be_partitioned(self):
        for solution in self.solutions:
            self.assertFalse(solution.canThreePartsEqualSum([1, 2, 3, 4]))

    def test_third_part_must_have_at_least_one_value(self):
        for solution in self.solutions:
            self.assertFalse(solution.canThreePartsEqualSum([1, 1, 1, 1, 1, 1, 6]))
