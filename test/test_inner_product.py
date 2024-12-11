from unittest import TestCase

from algorithm.dp.inner_product import Solution


class TestSolution(TestCase):
    def test_get_max_inner_product(self):
        tbt = Solution()
        cases = [
            ([2, 3, 5, 1], [2, 1], 7),
            ([1, 4, 3, 2, 5], [1, 2, 3, 4], 38),
        ]
        for A, B, exp in cases:
            with self.subTest(A=A, B=B, exp=exp):
                self.assertEqual(exp, tbt.getMaxInnerProduct(A, B))
                self.assertEqual(exp, tbt.getMaxInnerProduct2(A, B))
