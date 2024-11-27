"""binary search in python"""
import unittest
from bisect import bisect_left, bisect_right, insort_left


class TestBinarySearch(unittest.TestCase):
    """
    test binary search methods
    bisect is an alias of bisect_right
    """

    @classmethod
    def setUpClass(cls):
        """set up class var"""
        cls.TUPLE1 = (0, 1, 2, 3, 4, 6)  # length: 6

    def test_bisect_left_not_found(self):
        """5 not in list, should be inserted at index 5"""
        self.assertEqual(5, bisect_left(self.__class__.TUPLE1, 5))
        """-2 not in list, should be inserted at index 0"""
        self.assertEqual(0, bisect_left(self.__class__.TUPLE1, -2))
        """7 not in list, should be inserted at index 7"""
        self.assertEqual(6, bisect_left(self.__class__.TUPLE1, 7))

    def test_bisect_right_not_found(self):
        """7 not in list, should be inserted at index 6"""
        self.assertEqual(6, bisect_right(self.__class__.TUPLE1, 7))
        """5 not in list, should be inserted at index 5"""
        self.assertEqual(5, bisect_right(self.__class__.TUPLE1, 5))
        """-1 not in list, should be inserted at index 0"""
        self.assertEqual(0, bisect_right(self.__class__.TUPLE1, -1))

    def test_bisect_left_existing(self):
        """4 in list, new 4 should be inserted at index 4 on left of existing 4"""
        self.assertEqual(4, bisect_left(self.__class__.TUPLE1, 4))

    def test_bisect_left_existing_duplicate(self):
        """1 in list, should be inserted at index 1, left of all existing 1"""
        self.assertEqual(1, bisect_left([0, 1, 1, 1], 1))

    def test_bisect_right_existing(self):
        """2 in list, new 2 should be inserted at index 3"""
        self.assertEqual(3, bisect_right(self.__class__.TUPLE1, 2))

    def test_bisect_right_existing_duplicate(self):
        """1 in list, should insert at index 4, right of all existing 1"""
        self.assertEqual(4, bisect_right([0, 1, 1, 1], 1))

    def test_bisect_insort_left(self):
        """bisect left and then insert to keep sorted"""
        list1 = [1]
        list2 = [1]
        list3 = [[0], list1, [2]]
        insort_left(list3, list2, key=lambda l: l[0])
        self.assertEqual([[0], [1], [1], [2]], list3)
        self.assertTrue(list3[1] is list2)
        self.assertTrue(list3[2] is list1)


if __name__ == '__main__':
    unittest.main()
