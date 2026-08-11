import copy
import unittest

from algorithm.graph.shortest_bridge import Solution, Solution2


class TestShortestBridge(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        grid = [[0, 1], [1, 0]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(1, sol.shortestBridge(copy.deepcopy(grid)))

    def test_example2(self):
        grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(2, sol.shortestBridge(copy.deepcopy(grid)))

    def test_example3(self):
        grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(1, sol.shortestBridge(copy.deepcopy(grid)))

    def test_adjacent(self):
        """Two islands separated by single cell in 3x3."""
        grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(3, sol.shortestBridge(copy.deepcopy(grid)))

    def test_large_gap(self):
        grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(7, sol.shortestBridge(copy.deepcopy(grid)))

    def test_multi_cell_islands(self):
        grid = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(2, sol.shortestBridge(copy.deepcopy(grid)))


if __name__ == "__main__":
    unittest.main()
