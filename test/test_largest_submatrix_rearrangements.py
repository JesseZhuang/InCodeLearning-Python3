import unittest

from algorithm.jzarray.largest_submatrix_rearrangements import Solution1, Solution2


class TestLargestSubmatrixRearrangements(unittest.TestCase):

    def test_largest_submatrix(self):
        cases = [
            ([[0, 0, 1], [1, 1, 1], [1, 0, 1]], 4),
            ([[1, 0, 1, 0, 1]], 3),
            ([[1, 1, 0], [1, 0, 1]], 2),
            ([[0, 0], [0, 0]], 0),
            ([[1]], 1),
            ([[1, 1, 1], [1, 1, 1]], 6),
            ([[1], [1], [0], [1]], 2),
        ]
        tbt1, tbt2 = Solution1(), Solution2()
        for matrix, exp in cases:
            with self.subTest(matrix=matrix, exp=exp):
                self.assertEqual(tbt1.largestSubmatrix(matrix), exp)
                self.assertEqual(tbt2.largestSubmatrix(matrix), exp)
