import copy
from unittest import TestCase

from algorithm.jzarray.rotate_image import Solution, Solution2


class TestRotateImage(TestCase):
    def test_rotate(self):
        cases = [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
            ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
             [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
            ([[1]], [[1]]),
            ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
            ([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]],
             [[21, 16, 11, 6, 1],
              [22, 17, 12, 7, 2],
              [23, 18, 13, 8, 3],
              [24, 19, 14, 9, 4],
              [25, 20, 15, 10, 5]]),
        ]
        solutions = [Solution(), Solution2()]
        for matrix, exp in cases:
            for sol in solutions:
                with self.subTest(n=len(matrix), sol=sol.__class__.__name__):
                    m = copy.deepcopy(matrix)
                    sol.rotate(m)
                    self.assertEqual(m, exp)
