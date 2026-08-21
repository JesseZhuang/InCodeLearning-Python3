import unittest

from algorithm.binary_search.search_2d_matrix_ii import Solution


class TestSearch2DMatrixII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]
        for sol in self.solutions:
            self.assertTrue(sol.searchMatrix(matrix, 5))
            self.assertTrue(sol.searchMatrix2(matrix, 5))

    def test_example2(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]
        for sol in self.solutions:
            self.assertFalse(sol.searchMatrix(matrix, 20))
            self.assertFalse(sol.searchMatrix2(matrix, 20))

    def test_single_element_found(self):
        matrix = [[5]]
        for sol in self.solutions:
            self.assertTrue(sol.searchMatrix(matrix, 5))
            self.assertTrue(sol.searchMatrix2(matrix, 5))

    def test_single_element_not_found(self):
        matrix = [[5]]
        for sol in self.solutions:
            self.assertFalse(sol.searchMatrix(matrix, 3))
            self.assertFalse(sol.searchMatrix2(matrix, 3))

    def test_target_in_bottom_left(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]
        for sol in self.solutions:
            self.assertTrue(sol.searchMatrix(matrix, 18))
            self.assertTrue(sol.searchMatrix2(matrix, 18))

    def test_target_in_top_right(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]
        for sol in self.solutions:
            self.assertTrue(sol.searchMatrix(matrix, 15))
            self.assertTrue(sol.searchMatrix2(matrix, 15))

    def test_target_smaller_than_all(self):
        matrix = [[2, 4], [6, 8]]
        for sol in self.solutions:
            self.assertFalse(sol.searchMatrix(matrix, 1))
            self.assertFalse(sol.searchMatrix2(matrix, 1))

    def test_target_larger_than_all(self):
        matrix = [[2, 4], [6, 8]]
        for sol in self.solutions:
            self.assertFalse(sol.searchMatrix(matrix, 9))
            self.assertFalse(sol.searchMatrix2(matrix, 9))

    def test_single_row(self):
        matrix = [[1, 3, 5, 7, 9]]
        for sol in self.solutions:
            self.assertTrue(sol.searchMatrix(matrix, 7))
            self.assertTrue(sol.searchMatrix2(matrix, 7))
            self.assertFalse(sol.searchMatrix(matrix, 4))
            self.assertFalse(sol.searchMatrix2(matrix, 4))

    def test_single_column(self):
        matrix = [[1], [3], [5], [7]]
        for sol in self.solutions:
            self.assertTrue(sol.searchMatrix(matrix, 5))
            self.assertTrue(sol.searchMatrix2(matrix, 5))
            self.assertFalse(sol.searchMatrix(matrix, 4))
            self.assertFalse(sol.searchMatrix2(matrix, 4))

    def test_negative_values(self):
        matrix = [[-5, -3], [-1, 2]]
        for sol in self.solutions:
            self.assertTrue(sol.searchMatrix(matrix, -3))
            self.assertTrue(sol.searchMatrix2(matrix, -3))
            self.assertFalse(sol.searchMatrix(matrix, 0))
            self.assertFalse(sol.searchMatrix2(matrix, 0))


if __name__ == "__main__":
    unittest.main()
