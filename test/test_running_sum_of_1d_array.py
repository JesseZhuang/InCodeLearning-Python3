from unittest import TestCase

from algorithm.jzarray.running_sum_of_1d_array import Solution


class TestRunningSumOf1dArray(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_running_sum(self):
        cases = [
            ([1, 2, 3, 4], [1, 3, 6, 10]),
            ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
            ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
            ([7], [7]),
            ([0, 0, 0], [0, 0, 0]),
            ([-4, -3, -2], [-4, -7, -9]),
            ([-2, 5, -3, 0], [-2, 3, 0, 0]),
            ([10**6] * 1000, [10**6 * index for index in range(1, 1001)]),
        ]
        for original, expected in cases:
            for solution in self.solutions:
                with self.subTest(original=original[:4], solution=solution.__class__.__name__):
                    nums = original.copy()
                    result = solution.runningSum(nums)
                    self.assertEqual(result, expected)
                    self.assertIs(result, nums)
