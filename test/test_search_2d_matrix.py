import unittest

from algorithm.jzarray.search_2d_matrix import Solution


class TestSearch2DMatrix(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        for sol in self.solutions:
            self.assertTrue(sol.searchMatrix(matrix, 3))
            self.assertTrue(sol.searchMatrix2(matrix, 3))

    def test_example2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        for sol in self.solutions:
            self.assertFalse(sol.searchMatrix(matrix, 13))
            self.assertFalse(sol.searchMatrix2(matrix, 13))

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

    def test_first_element(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20]]
        for sol in self.solutions:
            self.assertTrue(sol.searchMatrix(matrix, 1))
            self.assertTrue(sol.searchMatrix2(matrix, 1))

    def test_last_element(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20]]
        for sol in self.solutions:
            self.assertTrue(sol.searchMatrix(matrix, 20))
            self.assertTrue(sol.searchMatrix2(matrix, 20))

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


if __name__ == "__main__":
    unittest.main()
