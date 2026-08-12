"""test LeetCode 221 Maximal Square"""
import unittest

from algorithm.dp.maximal_square import Solution


class TestMaximalSquare(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        for sol in self.solutions:
            self.assertEqual(4, sol.maximalSquare(matrix))

    def test_example2(self):
        matrix = [["0", "1"], ["1", "0"]]
        for sol in self.solutions:
            self.assertEqual(1, sol.maximalSquare(matrix))

    def test_all_zeros(self):
        matrix = [["0", "0"], ["0", "0"]]
        for sol in self.solutions:
            self.assertEqual(0, sol.maximalSquare(matrix))

    def test_single_one(self):
        matrix = [["1"]]
        for sol in self.solutions:
            self.assertEqual(1, sol.maximalSquare(matrix))

    def test_single_zero(self):
        matrix = [["0"]]
        for sol in self.solutions:
            self.assertEqual(0, sol.maximalSquare(matrix))

    def test_all_ones_3x3(self):
        matrix = [["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]]
        for sol in self.solutions:
            self.assertEqual(9, sol.maximalSquare(matrix))

    def test_single_row(self):
        matrix = [["1", "1", "1", "1"]]
        for sol in self.solutions:
            self.assertEqual(1, sol.maximalSquare(matrix))

    def test_single_column(self):
        matrix = [["1"], ["1"], ["1"]]
        for sol in self.solutions:
            self.assertEqual(1, sol.maximalSquare(matrix))

    def test_large_square_bottom_right(self):
        matrix = [
            ["0", "0", "0", "0"],
            ["0", "1", "1", "1"],
            ["0", "1", "1", "1"],
            ["0", "1", "1", "1"],
        ]
        for sol in self.solutions:
            self.assertEqual(9, sol.maximalSquare(matrix))

    def test_empty_matrix(self):
        for sol in self.solutions:
            self.assertEqual(0, sol.maximalSquare([]))


if __name__ == '__main__':
    unittest.main()
