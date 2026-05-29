import unittest
from algorithm.graph.pacific_atlantic_water_flow import Solution, Solution2


class TestPacificAtlantic(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        expected = {(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)}
        for sol in self.solutions:
            result = sol.pacificAtlantic(heights)
            self.assertEqual(set(map(tuple, result)), expected)

    def test_single_cell(self):
        heights = [[1]]
        expected = {(0, 0)}
        for sol in self.solutions:
            result = sol.pacificAtlantic(heights)
            self.assertEqual(set(map(tuple, result)), expected)

    def test_flat_grid(self):
        """All same height: every cell can reach both oceans."""
        heights = [[1, 1], [1, 1]]
        expected = {(0, 0), (0, 1), (1, 0), (1, 1)}
        for sol in self.solutions:
            result = sol.pacificAtlantic(heights)
            self.assertEqual(set(map(tuple, result)), expected)

    def test_increasing_slope(self):
        """Water flows only downhill, corner is highest."""
        heights = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = {(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)}
        for sol in self.solutions:
            result = sol.pacificAtlantic(heights)
            self.assertEqual(set(map(tuple, result)), expected)

    def test_single_row(self):
        heights = [[1, 2, 3, 4, 5]]
        expected = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)}
        for sol in self.solutions:
            result = sol.pacificAtlantic(heights)
            self.assertEqual(set(map(tuple, result)), expected)

    def test_single_column(self):
        heights = [[5], [4], [3], [2], [1]]
        expected = {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)}
        for sol in self.solutions:
            result = sol.pacificAtlantic(heights)
            self.assertEqual(set(map(tuple, result)), expected)


if __name__ == '__main__':
    unittest.main()
