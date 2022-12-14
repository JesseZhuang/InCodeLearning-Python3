# pylint: disable=missing-function-docstring
'''binary search in python'''
import unittest
from bisect import bisect_left, bisect_right


class TestBinarySearch(unittest.TestCase):
    '''binary search methods'''

    list1 = [0, 1, 2, 3, 4, 6]

    def test_bisect_left_not_found(self):
        self.assertEqual(5, bisect_left(self.__class__.list1, 5))

    def test_bisect_left_existing(self):
        self.assertEqual(4, bisect_left(self.__class__.list1, 4))

    def test_bisect_left_existing_duplicate(self):
        self.assertEqual(1, bisect_left([0, 1, 1, 1], 1))

    def test_bisect_left_found(self):
        self.assertEqual(2, bisect_left(self.__class__.list1, 2))

    def test_bisect_right_found(self):
        self.assertEqual(3, bisect_right(self.__class__.list1, 2))

    def test_bisect_right_existing(self):
        self.assertEqual(4, bisect_right([0, 1, 1, 1], 1))


if __name__ == '__main__':
    unittest.main()
