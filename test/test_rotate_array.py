import copy
from unittest import TestCase

from algorithm.jzarray.rotate_array import Solution, Solution2


class TestRotateArray(TestCase):
    def test_rotate(self):
        cases = [
            ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
            ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
            ([1], 0, [1]),
            ([1], 1, [1]),
            ([1, 2], 1, [2, 1]),
            ([1, 2], 2, [1, 2]),
            ([1, 2], 3, [2, 1]),
            ([1, 2, 3, 4, 5, 6, 7], 0, [1, 2, 3, 4, 5, 6, 7]),
            ([1, 2, 3, 4, 5, 6, 7], 7, [1, 2, 3, 4, 5, 6, 7]),
            ([1, 2, 3, 4, 5, 6, 7], 10, [5, 6, 7, 1, 2, 3, 4]),
        ]
        solutions = [Solution(), Solution2()]
        for nums, k, exp in cases:
            for sol in solutions:
                with self.subTest(nums=nums, k=k, sol=sol.__class__.__name__):
                    arr = copy.copy(nums)
                    sol.rotate(arr, k)
                    self.assertEqual(arr, exp)
