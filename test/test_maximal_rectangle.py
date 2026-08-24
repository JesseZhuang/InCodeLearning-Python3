import unittest

from algorithm.dp.maximal_rectangle import Solution, Solution2


class TestMaximalRectangle(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        for sol in self.solutions:
            self.assertEqual(sol.maximalRectangle(matrix), 6)

    def test_empty_matrix(self):
        for sol in self.solutions:
            self.assertEqual(sol.maximalRectangle([]), 0)
            self.assertEqual(sol.maximalRectangle([[]]), 0)

    def test_single_zero(self):
        for sol in self.solutions:
            self.assertEqual(sol.maximalRectangle([["0"]]), 0)

    def test_single_one(self):
        for sol in self.solutions:
            self.assertEqual(sol.maximalRectangle([["1"]]), 1)

    def test_all_ones(self):
        matrix = [["1", "1"], ["1", "1"], ["1", "1"]]
        for sol in self.solutions:
            self.assertEqual(sol.maximalRectangle(matrix), 6)

    def test_all_zeros(self):
        matrix = [["0", "0"], ["0", "0"]]
        for sol in self.solutions:
            self.assertEqual(sol.maximalRectangle(matrix), 0)

    def test_single_row(self):
        matrix = [["1", "1", "0", "1", "1", "1"]]
        for sol in self.solutions:
            self.assertEqual(sol.maximalRectangle(matrix), 3)

    def test_single_column(self):
        matrix = [["1"], ["1"], ["0"], ["1"]]
        for sol in self.solutions:
            self.assertEqual(sol.maximalRectangle(matrix), 2)

    def test_l_shape(self):
        matrix = [
            ["1", "0"],
            ["1", "0"],
            ["1", "1"],
        ]
        for sol in self.solutions:
            self.assertEqual(sol.maximalRectangle(matrix), 3)

    def test_wide_rectangle(self):
        matrix = [
            ["0", "1", "1", "1", "1"],
            ["0", "1", "1", "1", "1"],
            ["0", "0", "0", "0", "0"],
        ]
        for sol in self.solutions:
            self.assertEqual(sol.maximalRectangle(matrix), 8)


if __name__ == '__main__':
    unittest.main()
