'''binary search in python'''
import unittest
from bisect import bisect_left


class TestBinarySearch(unittest.TestCase):
    '''binary search methods'''

    list1 = [0, 1, 2, 3, 4, 6]

    def test_bisect_left_not_found(self):
        '''binary search left'''
        self.assertEqual(5, bisect_left(self.__class__.list1, 5))


if __name__ == '__main__':
    unittest.main()
