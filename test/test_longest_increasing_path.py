from unittest import TestCase

from algorithm.graph.longest_increasing_path import SolutionDFS, SolutionBFS


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [SolutionDFS(), SolutionBFS()]

    def test_longest_increasing_path(self):
        cases = [
            ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
            ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
            ([[1]], 1),
            ([[1, 2]], 2),
            ([[3, 2, 1], [6, 5, 4], [9, 8, 7]], 5),
            ([[7, 8, 9], [9, 7, 6], [7, 2, 3]], 6),
        ]
        for sol in self.solutions:
            for matrix, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, matrix=matrix, exp=exp):
                    self.assertEqual(sol.longestIncreasingPath(matrix), exp)

    def test_single_row(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestIncreasingPath([[1, 2, 3, 4, 5]]), 5)

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestIncreasingPath([[1, 1], [1, 1]]), 1)
