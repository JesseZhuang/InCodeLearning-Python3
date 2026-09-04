import unittest

from algorithm.jzarray.game_of_life import Solution, Solution2


class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
            sol.gameOfLife(board)
            self.assertEqual([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]], board)

    def test_example2(self):
        for sol in self.solutions:
            board = [[1, 1], [1, 0]]
            sol.gameOfLife(board)
            self.assertEqual([[1, 1], [1, 1]], board)

    def test_single_cell_dead(self):
        for sol in self.solutions:
            board = [[0]]
            sol.gameOfLife(board)
            self.assertEqual([[0]], board)

    def test_single_cell_alive(self):
        for sol in self.solutions:
            board = [[1]]
            sol.gameOfLife(board)
            self.assertEqual([[0]], board)

    def test_all_alive(self):
        for sol in self.solutions:
            board = [[1, 1], [1, 1]]
            sol.gameOfLife(board)
            self.assertEqual([[1, 1], [1, 1]], board)

    def test_all_dead(self):
        for sol in self.solutions:
            board = [[0, 0], [0, 0]]
            sol.gameOfLife(board)
            self.assertEqual([[0, 0], [0, 0]], board)

    def test_blinker(self):
        """Blinker oscillator: vertical bar toggles to horizontal."""
        for sol in self.solutions:
            board = [[0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0]]
            sol.gameOfLife(board)
            self.assertEqual([[0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 1, 1, 1, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]], board)

    def test_single_row(self):
        for sol in self.solutions:
            board = [[1, 1, 1]]
            sol.gameOfLife(board)
            self.assertEqual([[0, 1, 0]], board)

    def test_single_column(self):
        for sol in self.solutions:
            board = [[1], [1], [1]]
            sol.gameOfLife(board)
            self.assertEqual([[0], [1], [0]], board)
