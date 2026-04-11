import unittest

from algorithm.jzarray.merge_intervals import Solution


class TestMergeIntervals(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def verify(self, intervals, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.merge([i[:] for i in intervals])
                self.assertEqual(expected, result)

    def test_example1(self):
        self.verify([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])

    def test_example2(self):
        self.verify([[1, 4], [4, 5]], [[1, 5]])

    def test_single_interval(self):
        self.verify([[1, 1]], [[1, 1]])

    def test_no_overlap(self):
        self.verify([[1, 2], [4, 5], [7, 8]], [[1, 2], [4, 5], [7, 8]])

    def test_all_overlap(self):
        self.verify([[1, 10], [2, 3], [4, 5], [6, 7]], [[1, 10]])

    def test_unsorted_input(self):
        self.verify([[3, 4], [1, 2], [5, 6], [2, 3]], [[1, 4], [5, 6]])

    def test_nested_intervals(self):
        self.verify([[1, 5], [2, 3]], [[1, 5]])

    def test_touching_edges(self):
        self.verify([[1, 2], [2, 3], [3, 4]], [[1, 4]])
