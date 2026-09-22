import copy
import unittest

from algorithm.graph.zero_one_matrix import Solution, Solution2


class TestZeroOneMatrix(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.updateMatrix(copy.deepcopy(mat)), expected)

    def test_example2(self):
        mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.updateMatrix(copy.deepcopy(mat)), expected)

    def test_all_zeros(self):
        mat = [[0, 0], [0, 0]]
        expected = [[0, 0], [0, 0]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.updateMatrix(copy.deepcopy(mat)), expected)

    def test_single_one(self):
        mat = [[1, 0], [0, 0]]
        expected = [[1, 0], [0, 0]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.updateMatrix(copy.deepcopy(mat)), expected)

    def test_corner_ones(self):
        mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[2, 1, 2], [1, 0, 1], [2, 1, 2]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.updateMatrix(copy.deepcopy(mat)), expected)

    def test_single_cell_zero(self):
        mat = [[0]]
        expected = [[0]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.updateMatrix(copy.deepcopy(mat)), expected)

    def test_row(self):
        mat = [[1, 1, 0, 1, 1]]
        expected = [[2, 1, 0, 1, 2]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.updateMatrix(copy.deepcopy(mat)), expected)

    def test_column(self):
        mat = [[1], [1], [0], [1], [1]]
        expected = [[2], [1], [0], [1], [2]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.updateMatrix(copy.deepcopy(mat)), expected)

    def test_large_distance(self):
        mat = [[1, 1, 1, 1, 0]]
        expected = [[4, 3, 2, 1, 0]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.updateMatrix(copy.deepcopy(mat)), expected)


if __name__ == '__main__':
    unittest.main()
