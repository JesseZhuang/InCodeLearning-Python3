'''binary search in python'''
import unittest
from bisect import bisect_left, bisect_right


class TestBinarySearch(unittest.TestCase):
    '''binary search methods'''

    list1 = [0, 1, 2, 3, 4, 6]

    def test_bisect_left_not_found(self):
        '''5 not in list, should be inserted at index 5'''
        self.assertEqual(5, bisect_left(self.__class__.list1, 5))

    def test_bisect_left_existing(self):
        '''4 in list, new 4 should be inserted at index 4 on left of existing 4'''
        self.assertEqual(4, bisect_left(self.__class__.list1, 4))

    def test_bisect_left_existing_duplicate(self):
        '''1 in list, should be inserted at index 1, left of all existing 1'''
        self.assertEqual(1, bisect_left([0, 1, 1, 1], 1))

    def test_bisect_right_existing(self):
        '''2 in list, new 2 should be inserted at index 3'''
        self.assertEqual(3, bisect_right(self.__class__.list1, 2))

    def test_bisect_right_existing_duplicate(self):
        '''1 in list, should insert at index 4, right of all existing 1'''
        self.assertEqual(4, bisect_right([0, 1, 1, 1], 1))


if __name__ == '__main__':
    unittest.main()
