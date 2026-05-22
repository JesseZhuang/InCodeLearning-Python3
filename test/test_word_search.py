from unittest import TestCase

from algorithm.graph.word_search import Solution


class TestWordSearch(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        for s in self.solutions:
            self.assertTrue(s.exist([row[:] for row in board], "ABCCED"))

    def test_example2(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        for s in self.solutions:
            self.assertTrue(s.exist([row[:] for row in board], "SEE"))

    def test_example3(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        for s in self.solutions:
            self.assertFalse(s.exist([row[:] for row in board], "ABCB"))

    def test_single_cell_true(self):
        board = [["A"]]
        for s in self.solutions:
            self.assertTrue(s.exist([row[:] for row in board], "A"))

    def test_single_cell_false(self):
        board = [["A"]]
        for s in self.solutions:
            self.assertFalse(s.exist([row[:] for row in board], "B"))

    def test_full_board(self):
        board = [["A", "B"], ["C", "D"]]
        for s in self.solutions:
            self.assertTrue(s.exist([row[:] for row in board], "ABDC"))

    def test_no_match_longer_word(self):
        board = [["A", "B"], ["C", "D"]]
        for s in self.solutions:
            self.assertFalse(s.exist([row[:] for row in board], "ABCDE"))
