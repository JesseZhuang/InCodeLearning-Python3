"""Tests for LeetCode 547. Number of Provinces."""

import unittest

from algorithm.graph.number_of_provinces import Solution, Solution2


class TestNumberOfProvinces(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        """Three cities, two connected -> 2 provinces."""
        for sol in self.solutions:
            grid = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
            self.assertEqual(sol.findCircleNum(grid), 2)

    def test_example2(self):
        """Three cities, none connected to each other -> 3 provinces."""
        for sol in self.solutions:
            grid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            self.assertEqual(sol.findCircleNum(grid), 3)

    def test_all_connected(self):
        """All cities connected -> 1 province."""
        for sol in self.solutions:
            grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            self.assertEqual(sol.findCircleNum(grid), 1)

    def test_single_city(self):
        """Single city -> 1 province."""
        for sol in self.solutions:
            grid = [[1]]
            self.assertEqual(sol.findCircleNum(grid), 1)

    def test_chain(self):
        """Chain: 0-1, 1-2, 2-3 -> 1 province."""
        for sol in self.solutions:
            grid = [
                [1, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 1, 1],
                [0, 0, 1, 1],
            ]
            self.assertEqual(sol.findCircleNum(grid), 1)

    def test_two_components(self):
        """4 cities, two pairs -> 2 provinces."""
        for sol in self.solutions:
            grid = [
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1],
            ]
            self.assertEqual(sol.findCircleNum(grid), 2)

    def test_large_isolated(self):
        """n=5, all isolated -> 5 provinces."""
        for sol in self.solutions:
            n = 5
            grid = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            self.assertEqual(sol.findCircleNum(grid), 5)


if __name__ == "__main__":
    unittest.main()
