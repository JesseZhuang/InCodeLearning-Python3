import unittest

from algorithm.jzarray.spiral_matrix import Solution, Solution2


class TestSpiralMatrix(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_3x3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        for sol in self.solutions:
            self.assertEqual(sol.spiralOrder(matrix), expected)

    def test_3x4(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        for sol in self.solutions:
            self.assertEqual(sol.spiralOrder(matrix), expected)

    def test_single_row(self):
        matrix = [[1, 2, 3, 4]]
        expected = [1, 2, 3, 4]
        for sol in self.solutions:
            self.assertEqual(sol.spiralOrder(matrix), expected)

    def test_single_column(self):
        matrix = [[1], [2], [3]]
        expected = [1, 2, 3]
        for sol in self.solutions:
            self.assertEqual(sol.spiralOrder(matrix), expected)

    def test_single_element(self):
        matrix = [[7]]
        expected = [7]
        for sol in self.solutions:
            self.assertEqual(sol.spiralOrder(matrix), expected)

    def test_2x2(self):
        matrix = [[1, 2], [3, 4]]
        expected = [1, 2, 4, 3]
        for sol in self.solutions:
            self.assertEqual(sol.spiralOrder(matrix), expected)

    def test_4x3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        expected = [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
        for sol in self.solutions:
            self.assertEqual(sol.spiralOrder(matrix), expected)


if __name__ == '__main__':
    unittest.main()
