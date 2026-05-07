import unittest

from algorithm.deq.largest_rectangle_histogram import Solution, Solution2


class TestLargestRectangleHistogram(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, heights, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.largestRectangleArea(heights))

    def test_example1(self):
        self.verify([2, 1, 5, 6, 2, 3], 10)

    def test_example2(self):
        self.verify([2, 4], 4)

    def test_single(self):
        self.verify([5], 5)

    def test_increasing(self):
        self.verify([1, 2, 3, 4, 5], 9)

    def test_decreasing(self):
        self.verify([5, 4, 3, 2, 1], 9)

    def test_all_same(self):
        self.verify([3, 3, 3, 3], 12)

    def test_valley(self):
        self.verify([6, 2, 5, 4, 5, 1, 6], 12)

    def test_zeros(self):
        self.verify([0, 0, 0], 0)

    def test_single_tall(self):
        self.verify([0, 9, 0], 9)

    def test_two_peaks(self):
        self.verify([1, 3, 2, 3, 1], 6)
