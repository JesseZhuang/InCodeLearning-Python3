import unittest

from algorithm.jzarray.set_matrix_zeroes import Solution, Solution2


class TestSetMatrixZeroes(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
            sol.setZeroes(matrix)
            self.assertEqual([[1, 0, 1], [0, 0, 0], [1, 0, 1]], matrix)

    def test_example2(self):
        for sol in self.solutions:
            matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
            sol.setZeroes(matrix)
            self.assertEqual([[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], matrix)

    def test_no_zeroes(self):
        for sol in self.solutions:
            matrix = [[1, 2], [3, 4]]
            sol.setZeroes(matrix)
            self.assertEqual([[1, 2], [3, 4]], matrix)

    def test_all_zeroes(self):
        for sol in self.solutions:
            matrix = [[0, 0], [0, 0]]
            sol.setZeroes(matrix)
            self.assertEqual([[0, 0], [0, 0]], matrix)

    def test_single_element_zero(self):
        for sol in self.solutions:
            matrix = [[0]]
            sol.setZeroes(matrix)
            self.assertEqual([[0]], matrix)

    def test_single_element_nonzero(self):
        for sol in self.solutions:
            matrix = [[5]]
            sol.setZeroes(matrix)
            self.assertEqual([[5]], matrix)

    def test_first_row_zero(self):
        for sol in self.solutions:
            matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            sol.setZeroes(matrix)
            self.assertEqual([[0, 0, 0], [0, 4, 5], [0, 7, 8]], matrix)

    def test_first_col_zero(self):
        for sol in self.solutions:
            matrix = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]
            sol.setZeroes(matrix)
            self.assertEqual([[0, 2, 3], [0, 0, 0], [0, 7, 8]], matrix)

    def test_corner_zero(self):
        for sol in self.solutions:
            matrix = [[0, 1], [1, 1]]
            sol.setZeroes(matrix)
            self.assertEqual([[0, 0], [0, 1]], matrix)

    def test_negative_values(self):
        for sol in self.solutions:
            matrix = [[-1, 0, 3], [4, 5, 6], [7, 8, 0]]
            sol.setZeroes(matrix)
            self.assertEqual([[0, 0, 0], [4, 0, 0], [0, 0, 0]], matrix)
