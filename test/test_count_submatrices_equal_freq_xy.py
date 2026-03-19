import unittest

from algorithm.jzarray.count_submatrices_equal_freq_xy import Solution


class TestCountSubmatricesEqualFreqXY(unittest.TestCase):

    def test_count_submatrices(self):
        cases = [
            ([["X", "Y", "."], ["Y", ".", "."]], 3),
            ([["X", "X"], ["X", "Y"]], 0),
            ([[".", "."]], 0),
            ([["X", "Y"]], 1),
            ([["X"], ["Y"]], 1),
            ([["Y", "X"]], 1),
            ([["X"]], 0),
            ([["Y"]], 0),
            ([[".", "X", ".", "Y"]], 1),
            ([["X", ".", "Y", ".", "X", "Y"]], 3),
            ([["X", "Y"], ["Y", "X"]], 3),
            ([[".", "."], [".", "."]], 0),
            ([["X", "Y", "X"], ["Y", "X", "Y"], ["X", "Y", "X"]], 5),
        ]
        tbt = Solution()
        for grid, exp in cases:
            with self.subTest(grid=grid, exp=exp):
                self.assertEqual(exp, tbt.numberOfSubmatrices(grid))
