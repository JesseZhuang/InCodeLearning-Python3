"""test LeetCode 64 Minimum Path Sum"""
import copy
import unittest

from algorithm.dp.minimum_path_sum import Solution, Solution2


class TestMinimumPathSum(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        for sol in self.solutions:
            self.assertEqual(7, sol.minPathSum(copy.deepcopy(grid)))

    def test_single_cell(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.minPathSum([[5]]))

    def test_single_row(self):
        grid = [[1, 2, 3]]
        for sol in self.solutions:
            self.assertEqual(6, sol.minPathSum(copy.deepcopy(grid)))

    def test_single_column(self):
        grid = [[1], [2], [3]]
        for sol in self.solutions:
            self.assertEqual(6, sol.minPathSum(copy.deepcopy(grid)))

    def test_two_by_two(self):
        grid = [[1, 2], [1, 1]]
        for sol in self.solutions:
            self.assertEqual(3, sol.minPathSum(copy.deepcopy(grid)))

    def test_all_zeros(self):
        grid = [[0, 0], [0, 0]]
        for sol in self.solutions:
            self.assertEqual(0, sol.minPathSum(copy.deepcopy(grid)))

    def test_large_values(self):
        grid = [[100, 100, 100], [100, 1, 100], [100, 1, 1]]
        for sol in self.solutions:
            self.assertEqual(203, sol.minPathSum(copy.deepcopy(grid)))

    def test_prefer_down_then_right(self):
        grid = [[1, 100], [1, 1]]
        for sol in self.solutions:
            self.assertEqual(3, sol.minPathSum(copy.deepcopy(grid)))
