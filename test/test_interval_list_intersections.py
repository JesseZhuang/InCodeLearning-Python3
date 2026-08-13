import unittest

from algorithm.jzarray.interval_list_intersections import Solution


class TestIntervalListIntersections(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def verify(self, first, second, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.intervalIntersection(
                    [i[:] for i in first], [i[:] for i in second]
                )
                self.assertEqual(expected, result)

    def test_example1(self):
        self.verify(
            [[0, 2], [5, 10], [13, 23], [24, 25]],
            [[1, 5], [8, 12], [15, 24], [25, 26]],
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        )

    def test_example2(self):
        self.verify([[1, 3], [5, 9]], [], [])

    def test_both_empty(self):
        self.verify([], [], [])

    def test_no_intersection(self):
        self.verify([[1, 2], [5, 6]], [[3, 4], [7, 8]], [])

    def test_full_overlap(self):
        self.verify([[0, 10]], [[0, 10]], [[0, 10]])

    def test_one_contains_other(self):
        self.verify([[0, 10]], [[2, 5], [7, 8]], [[2, 5], [7, 8]])

    def test_touching_endpoints(self):
        self.verify([[1, 3], [5, 7]], [[3, 5]], [[3, 3], [5, 5]])

    def test_single_point_intervals(self):
        self.verify([[1, 1], [3, 3]], [[1, 1], [2, 2], [3, 3]], [[1, 1], [3, 3]])
