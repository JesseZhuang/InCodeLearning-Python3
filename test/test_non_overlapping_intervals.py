import unittest

from algorithm.jzarray.non_overlapping_intervals import Solution


class TestNonOverlappingIntervals(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
            self.assertEqual(s.eraseOverlapIntervals2([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)

    def test_example2(self):
        for s in self.solutions:
            self.assertEqual(s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]), 2)
            self.assertEqual(s.eraseOverlapIntervals2([[1, 2], [1, 2], [1, 2]]), 2)

    def test_example3(self):
        for s in self.solutions:
            self.assertEqual(s.eraseOverlapIntervals([[1, 2], [2, 3]]), 0)
            self.assertEqual(s.eraseOverlapIntervals2([[1, 2], [2, 3]]), 0)

    def test_single_interval(self):
        for s in self.solutions:
            self.assertEqual(s.eraseOverlapIntervals([[1, 5]]), 0)
            self.assertEqual(s.eraseOverlapIntervals2([[1, 5]]), 0)

    def test_all_overlapping(self):
        for s in self.solutions:
            self.assertEqual(s.eraseOverlapIntervals([[1, 4], [2, 5], [3, 6]]), 2)
            self.assertEqual(s.eraseOverlapIntervals2([[1, 4], [2, 5], [3, 6]]), 2)

    def test_nested_intervals(self):
        for s in self.solutions:
            self.assertEqual(s.eraseOverlapIntervals([[1, 10], [2, 3], [4, 5], [6, 7]]), 1)
            self.assertEqual(s.eraseOverlapIntervals2([[1, 10], [2, 3], [4, 5], [6, 7]]), 1)

    def test_negative_bounds(self):
        for s in self.solutions:
            self.assertEqual(s.eraseOverlapIntervals([[-5, -3], [-4, -1], [0, 2]]), 1)
            self.assertEqual(s.eraseOverlapIntervals2([[-5, -3], [-4, -1], [0, 2]]), 1)


if __name__ == '__main__':
    unittest.main()
