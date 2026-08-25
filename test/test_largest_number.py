from unittest import TestCase

from algorithm.jzarray.largest_number import Solution


class TestSolution(TestCase):
    def test_largest_number(self):
        cases = [
            ([10, 2], "210"),
            ([3, 30, 34, 5, 9], "9534330"),
            ([1], "1"),
            ([0, 0], "0"),
            ([0, 0, 0, 0], "0"),
            ([10, 10], "1010"),
            ([999999998, 999999997, 999999999], "999999999999999998999999997"),
            ([34323, 3432], "343234323"),
            ([12, 121], "12121"),
            ([0, 9, 8, 7, 6, 5, 4, 3, 2, 1], "9876543210"),
        ]
        tbt = Solution()
        for nums, exp in cases:
            with self.subTest(nums=nums, exp=exp):
                self.assertEqual(tbt.largestNumber(nums), exp)
