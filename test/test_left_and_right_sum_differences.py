from unittest import TestCase

from algorithm.jzarray.left_and_right_sum_differences import Solution


class TestLeftAndRightSumDifferences(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_left_right_difference(self):
        cases = [
            ([10, 4, 8, 3], [15, 1, 11, 22]),
            ([1], [0]),
            ([5, 5], [5, 5]),
            ([1, 2, 3], [5, 2, 3]),
            ([100_000] * 1000, [abs(999 - 2 * index) * 100_000 for index in range(1000)]),
        ]
        for nums, expected in cases:
            for solution in self.solutions:
                with self.subTest(nums=nums[:4]):
                    self.assertEqual(solution.leftRightDifference(nums), expected)
