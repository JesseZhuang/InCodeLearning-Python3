import unittest

from algorithm.heap.min_time_mountain import Solution


class MinTimeMountainTest(unittest.TestCase):

    def setUp(self):
        self.tbt = Solution()
        self.cases = [
            [4, [2, 1, 1], 3],
            [10, [3, 2, 2, 4], 12],
            [5, [1], 15],
            [5, [1, 5], 10],
            [5, [1, 7], 10]
        ]

    def test_solution(self):
        for mh, w_times, exp in self.cases:
            self.assertEqual(exp, self.tbt.minNumberOfSeconds(mh, w_times))
