import copy
import unittest

from algorithm.graph.number_of_islands import Solution, Solution2


class TestNumIslands(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, grid, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                g = copy.deepcopy(grid)
                self.assertEqual(expected, sol.numIslands(g))

    def test_example1(self):
        self.verify([
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
        ], 1)

    def test_example2(self):
        self.verify([
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1'],
        ], 3)

    def test_empty(self):
        self.verify([], 0)

    def test_single_cell_island(self):
        self.verify([['1']], 1)

    def test_single_cell_water(self):
        self.verify([['0']], 0)

    def test_all_water(self):
        self.verify([['0', '0'], ['0', '0']], 0)

    def test_all_land(self):
        self.verify([['1', '1'], ['1', '1']], 1)

    def test_diagonal_not_connected(self):
        self.verify([
            ['1', '0'],
            ['0', '1'],
        ], 2)

    def test_single_row(self):
        self.verify([['1', '0', '1', '0', '1']], 3)

    def test_single_column(self):
        self.verify([['1'], ['0'], ['1'], ['0'], ['1']], 3)
