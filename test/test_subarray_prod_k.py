from unittest import TestCase

from algorithm.sliding.subarray_prod_k import Solution, Solution2


class TestSolution(TestCase):
    def test_num_subarray_product_less_than_k(self):
        cases = [
            ([10, 5, 2, 6], 100, 8),
            ([4, 13, 20, 32, 44, 59, 61, 71, 75, 86, 88], 567601, 32),
            ([1, 2, 3], 7, 6),
            ([2, 3, 4], 7, 4),
            ([1, 2, 3], 4, 4),
            ([1, 2, 3], 0, 0),
        ]
        tbt, tbt2 = Solution(), Solution2()
        for arr, k, exp in cases:
            with self.subTest(arr=arr, k=k, exp=exp):
                self.assertEqual(tbt.numSubarrayProductLessThanK(arr, k), exp)
                self.assertEqual(tbt2.numSubarrayProductLessThanK(arr, k), exp)
