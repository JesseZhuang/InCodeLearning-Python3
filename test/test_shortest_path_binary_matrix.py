import unittest
import copy

from algorithm.graph.shortest_path_binary_matrix import Solution, Solution2


class TestShortestPathBinaryMatrix(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for s in self.solutions:
            grid = [[0, 1], [1, 0]]
            self.assertEqual(2, s.shortestPathBinaryMatrix(copy.deepcopy(grid)))

    def test_example2(self):
        for s in self.solutions:
            grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
            self.assertEqual(4, s.shortestPathBinaryMatrix(copy.deepcopy(grid)))

    def test_example3(self):
        for s in self.solutions:
            grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
            self.assertEqual(-1, s.shortestPathBinaryMatrix(copy.deepcopy(grid)))

    def test_single_cell(self):
        for s in self.solutions:
            grid = [[0]]
            self.assertEqual(1, s.shortestPathBinaryMatrix(copy.deepcopy(grid)))

    def test_blocked_end(self):
        for s in self.solutions:
            grid = [[0, 0], [0, 1]]
            self.assertEqual(-1, s.shortestPathBinaryMatrix(copy.deepcopy(grid)))

    def test_no_path(self):
        for s in self.solutions:
            grid = [[0, 1, 0], [1, 1, 0], [0, 0, 0]]
            self.assertEqual(-1, s.shortestPathBinaryMatrix(copy.deepcopy(grid)))

    def test_large_open(self):
        for s in self.solutions:
            grid = [[0] * 5 for _ in range(5)]
            self.assertEqual(5, s.shortestPathBinaryMatrix(copy.deepcopy(grid)))

    def test_diagonal_path(self):
        for s in self.solutions:
            grid = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
            self.assertEqual(3, s.shortestPathBinaryMatrix(copy.deepcopy(grid)))


if __name__ == "__main__":
    unittest.main()
