import unittest

from algorithm.jzarray.trapping_rain_water import Solution, Solution2


class TestTrappingRainWater(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, height, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.trap(height))

    def test_example1(self):
        self.verify([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)

    def test_example2(self):
        self.verify([4, 2, 0, 3, 2, 5], 9)

    def test_empty(self):
        self.verify([], 0)

    def test_single(self):
        self.verify([5], 0)

    def test_two(self):
        self.verify([3, 1], 0)

    def test_no_trap(self):
        self.verify([1, 2, 3, 4, 5], 0)

    def test_descending(self):
        self.verify([5, 4, 3, 2, 1], 0)

    def test_valley(self):
        self.verify([3, 0, 3], 3)

    def test_all_same(self):
        self.verify([2, 2, 2, 2], 0)

    def test_large_valley(self):
        self.verify([5, 0, 0, 0, 5], 15)

    def test_multiple_valleys(self):
        self.verify([3, 0, 2, 0, 4], 7)
