from unittest import TestCase

from algorithm.jzarray.product_except_self import Solution, Solution2


class TestSolution(TestCase):
    def test_product_except_self(self):
        cases = [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
            ([0, 0], [0, 0]),
            ([1, 0], [0, 1]),
            ([2, 3], [3, 2]),
            ([1, 1, 1, 1], [1, 1, 1, 1]),
            ([5], [1]),
            ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        ]
        tbt, tbt2 = Solution(), Solution2()
        for nums, exp in cases:
            with self.subTest(nums=nums, exp=exp):
                self.assertEqual(tbt.productExceptSelf(nums), exp)
                self.assertEqual(tbt2.productExceptSelf(nums), exp)
