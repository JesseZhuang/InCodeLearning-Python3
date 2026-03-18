import unittest

from algorithm.jzarray.count_submatrices_top_left_le_k import Solution


class TestCountSubmatricesTopLeftLeK(unittest.TestCase):

    def test_count_submatrices(self):
        cases = [
            ([[7, 6, 3], [6, 6, 1]], 18, 4),
            ([[7, 2, 9], [1, 5, 0], [2, 6, 6]], 20, 6),
            ([[1]], 1, 1),
            ([[1]], 0, 0),
            ([[0, 0], [0, 0]], 0, 4),
            ([[1, 2, 3], [4, 5, 6]], 7, 4),
        ]
        tbt = Solution()
        for grid, k, exp in cases:
            with self.subTest(grid=grid, k=k, exp=exp):
                grid_copy = [row[:] for row in grid]
                self.assertEqual(exp, tbt.countSubmatrices(grid_copy, k))
