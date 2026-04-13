from unittest import TestCase

from algorithm.dp.max_prod_subarray import Solution


class TestSolution(TestCase):
    def test_max_product(self):
        cases = [
            ([2, 3, -2, 4], 6),
            ([-2, 0, -1], 0),
            ([-2], -2),
            ([0, 2], 2),
            ([-2, 3, -4], 24),
            ([2, -5, -2, -4, 3], 24),
            ([-1, -2, -3, 0], 6),
            ([1, -2, 3, -4, -3, -2, 1], 144),
        ]
        tbt = Solution()
        for nums, exp in cases:
            with self.subTest(nums=nums, exp=exp):
                self.assertEqual(tbt.maxProduct(nums), exp)
