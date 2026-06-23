import unittest

from algorithm.graph.surrounded_regions import Solution, Solution2


class TestSurroundedRegions(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            board = [
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'X'],
            ]
            sol.solve(board)
            expected = [
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'X', 'X'],
            ]
            self.assertEqual(board, expected)

    def test_single_cell(self):
        for sol in self.solutions:
            board = [['X']]
            sol.solve(board)
            self.assertEqual(board, [['X']])

    def test_all_o_on_border(self):
        for sol in self.solutions:
            board = [
                ['O', 'O'],
                ['O', 'O'],
            ]
            sol.solve(board)
            expected = [
                ['O', 'O'],
                ['O', 'O'],
            ]
            self.assertEqual(board, expected)

    def test_no_o(self):
        for sol in self.solutions:
            board = [
                ['X', 'X'],
                ['X', 'X'],
            ]
            sol.solve(board)
            expected = [
                ['X', 'X'],
                ['X', 'X'],
            ]
            self.assertEqual(board, expected)

    def test_inner_surrounded(self):
        for sol in self.solutions:
            board = [
                ['X', 'X', 'X'],
                ['X', 'O', 'X'],
                ['X', 'X', 'X'],
            ]
            sol.solve(board)
            expected = [
                ['X', 'X', 'X'],
                ['X', 'X', 'X'],
                ['X', 'X', 'X'],
            ]
            self.assertEqual(board, expected)

    def test_connected_to_border(self):
        for sol in self.solutions:
            board = [
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'O', 'X', 'X'],
                ['X', 'X', 'X', 'O'],
            ]
            sol.solve(board)
            expected = [
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'O'],
            ]
            self.assertEqual(board, expected)

    def test_single_row(self):
        for sol in self.solutions:
            board = [['X', 'O', 'X', 'O', 'X']]
            sol.solve(board)
            self.assertEqual(board, [['X', 'O', 'X', 'O', 'X']])

    def test_single_column(self):
        for sol in self.solutions:
            board = [['X'], ['O'], ['X'], ['O'], ['X']]
            sol.solve(board)
            self.assertEqual(board, [['X'], ['O'], ['X'], ['O'], ['X']])


if __name__ == '__main__':
    unittest.main()
