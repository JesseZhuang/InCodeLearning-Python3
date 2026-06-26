import unittest

from algorithm.binary_search.median_two_sorted_arrays import Solution, Solution2


class TestMedianTwoSortedArrays(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for s in self.solutions:
            self.assertAlmostEqual(s.findMedianSortedArrays([1, 3], [2]), 2.0)

    def test_example2(self):
        for s in self.solutions:
            self.assertAlmostEqual(s.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    def test_empty_first(self):
        for s in self.solutions:
            self.assertAlmostEqual(s.findMedianSortedArrays([], [1]), 1.0)

    def test_empty_second(self):
        for s in self.solutions:
            self.assertAlmostEqual(s.findMedianSortedArrays([2], []), 2.0)

    def test_single_elements(self):
        for s in self.solutions:
            self.assertAlmostEqual(s.findMedianSortedArrays([1], [2]), 1.5)

    def test_odd_total(self):
        for s in self.solutions:
            self.assertAlmostEqual(s.findMedianSortedArrays([1, 2], [3, 4, 5]), 3.0)

    def test_same_elements(self):
        for s in self.solutions:
            self.assertAlmostEqual(s.findMedianSortedArrays([1, 1, 1], [1, 1, 1]), 1.0)

    def test_large_gap(self):
        for s in self.solutions:
            self.assertAlmostEqual(s.findMedianSortedArrays([1, 2], [100, 200]), 51.0)

    def test_one_element_vs_many(self):
        for s in self.solutions:
            self.assertAlmostEqual(s.findMedianSortedArrays([3], [1, 2, 4, 5, 6]), 3.5)

    def test_negative_numbers(self):
        for s in self.solutions:
            self.assertAlmostEqual(s.findMedianSortedArrays([-5, -3, -1], [0, 2, 4]), -0.5)


if __name__ == '__main__':
    unittest.main()
