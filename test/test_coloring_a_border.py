import copy
import unittest

from algorithm.graph.coloring_a_border import Solution


class TestColoringABorder(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def verify(self, grid, row, col, color, expected):
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(expected, solution.colorBorder(copy.deepcopy(grid), row, col, color))

    def test_mixed_grid(self):
        self.verify([[1, 1], [1, 2]], 0, 0, 3, [[3, 3], [3, 2]])

    def test_interior_is_not_colored(self):
        self.verify([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2,
                    [[2, 2, 2], [2, 1, 2], [2, 2, 2]])

    def test_border_next_to_different_color(self):
        grid = [[1] * 5 for _ in range(5)]
        grid[2][2] = 2
        expected = [[3 if row in (0, 4) or col in (0, 4) or abs(row - 2) + abs(col - 2) == 1
                     else grid[row][col] for col in range(5)] for row in range(5)]
        self.verify(grid, 1, 1, 3, expected)

    def test_only_connected_component_changes(self):
        self.verify([[1, 2, 1], [2, 2, 2], [1, 2, 1]], 0, 0, 3,
                    [[3, 2, 1], [2, 2, 2], [1, 2, 1]])

    def test_same_color_noop(self):
        self.verify([[1, 1], [1, 2]], 0, 0, 1, [[1, 1], [1, 2]])

    def test_single_cell_and_single_row(self):
        self.verify([[8]], 0, 0, 1000, [[1000]])
        self.verify([[1, 1, 1, 1]], 0, 2, 4, [[4, 4, 4, 4]])

    def test_largest_grid_keeps_deep_interior(self):
        grid = [[1] * 50 for _ in range(50)]
        expected = [[2 if row in (0, 49) or col in (0, 49) else 1
                     for col in range(50)] for row in range(50)]
        self.verify(grid, 25, 25, 2, expected)


if __name__ == '__main__':
    unittest.main()
