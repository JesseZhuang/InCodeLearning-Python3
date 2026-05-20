import unittest

from algorithm.graph.rotting_oranges import Solution


class TestRottingOranges(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for s in self.solutions:
            grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
            self.assertEqual(4, s.orangesRotting(grid))

    def test_example2(self):
        for s in self.solutions:
            grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
            self.assertEqual(-1, s.orangesRotting(grid))

    def test_no_fresh(self):
        for s in self.solutions:
            grid = [[0, 2]]
            self.assertEqual(0, s.orangesRotting(grid))

    def test_all_empty(self):
        for s in self.solutions:
            grid = [[0]]
            self.assertEqual(0, s.orangesRotting(grid))

    def test_single_fresh(self):
        for s in self.solutions:
            grid = [[1]]
            self.assertEqual(-1, s.orangesRotting(grid))

    def test_single_rotten(self):
        for s in self.solutions:
            grid = [[2]]
            self.assertEqual(0, s.orangesRotting(grid))

    def test_already_all_rotten(self):
        for s in self.solutions:
            grid = [[2, 2], [2, 2]]
            self.assertEqual(0, s.orangesRotting(grid))

    def test_large_grid(self):
        for s in self.solutions:
            grid = [[2, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
            self.assertEqual(6, s.orangesRotting(grid))


if __name__ == '__main__':
    unittest.main()
