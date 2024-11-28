from unittest import TestCase

from algorithm.bit.xor_operations import xor_operations, xor_operations_1


class TestXorOperations(TestCase):
    def test_xor_operations(self):
        cases = [
            ([10, 20], 1, [30, 20]),
            ([10, 20], 2, [30, 10]),
            ([10, 20], 3, [20, 10]),
            ([10, 20], 4, [20, 30]),
            ([10, 20], 5, [10, 30]),
            ([10, 20], 6, [10, 20]),
            ([10, 20], 7, [30, 20]),
            ([10, 20], 8, [30, 10]),
            ([6, 1, 9], 1, [15, 1, 9]),
            ([6, 1, 9], 2, [15, 0, 9]),
            ([6, 1, 9], 3, [15, 0, 6]),
            ([6, 1, 9], 4, [9, 0, 6]),
            ([6, 1, 9], 5, [9, 0, 6]),
            ([6, 1, 9], 6, [9, 0, 15]),
            ([6, 1, 9], 7, [6, 0, 15]),
            ([6, 1, 9], 8, [6, 0, 15]),
            ([6, 1, 9], 9, [6, 0, 9]),
            ([6, 1, 9], 10, [15, 0, 9]),
            ([1, 2], 2, [3, 1]),
            ([5, 6, 7, 8], 3, [13, 1, 6, 8]),
            ([2], 1, [0]),
            ([2], 2, [0]),
            ([1, 2, 3, 4, 5], 1, [4, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 3, [4, 6, 0, 4, 5]),
        ]
        for arr, k, exp in cases:
            with self.subTest(arr=arr, k=k, exp=exp):
                self.assertEqual(exp, xor_operations(arr.copy(), k))
                self.assertEqual(exp, xor_operations_1(arr.copy(), k))
