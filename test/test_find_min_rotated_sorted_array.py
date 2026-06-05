import unittest

from algorithm.jzarray.find_min_rotated_sorted_array import Solution, Solution2


class TestFindMinRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(s.findMin([3, 4, 5, 1, 2]), 1)

    def test_example2(self):
        for s in self.solutions:
            self.assertEqual(s.findMin([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_not_rotated(self):
        for s in self.solutions:
            self.assertEqual(s.findMin([11, 13, 15, 17]), 11)

    def test_single_element(self):
        for s in self.solutions:
            self.assertEqual(s.findMin([1]), 1)

    def test_two_elements_rotated(self):
        for s in self.solutions:
            self.assertEqual(s.findMin([2, 1]), 1)

    def test_two_elements_not_rotated(self):
        for s in self.solutions:
            self.assertEqual(s.findMin([1, 2]), 1)

    def test_rotated_once(self):
        for s in self.solutions:
            self.assertEqual(s.findMin([7, 1, 2, 3, 4, 5, 6]), 1)

    def test_negative_numbers(self):
        for s in self.solutions:
            self.assertEqual(s.findMin([1, 2, 3, -5, -4, -3, -2, -1, 0]), -5)


if __name__ == "__main__":
    unittest.main()
