import unittest

from algorithm.stack.evaluate_reverse_polish_notation import Solution


class TestEvalRPN(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        """["2","1","+","3","*"] -> 9"""
        for sol in self.solutions:
            self.assertEqual(9, sol.evalRPN(["2", "1", "+", "3", "*"]))

    def test_example2(self):
        """["4","13","5","/","+"] -> 6"""
        for sol in self.solutions:
            self.assertEqual(6, sol.evalRPN(["4", "13", "5", "/", "+"]))

    def test_example3(self):
        """["10","6","9","3","+","-11","*","/","*","17","+","5","+"] -> 22"""
        for sol in self.solutions:
            self.assertEqual(
                22,
                sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]),
            )

    def test_single_number(self):
        for sol in self.solutions:
            self.assertEqual(42, sol.evalRPN(["42"]))

    def test_negative_result(self):
        """["1","2","-"] -> -1"""
        for sol in self.solutions:
            self.assertEqual(-1, sol.evalRPN(["1", "2", "-"]))

    def test_division_truncates_toward_zero(self):
        """["7","-3","/"] -> -2 (truncate toward zero, not floor)"""
        for sol in self.solutions:
            self.assertEqual(-2, sol.evalRPN(["7", "-3", "/"]))

    def test_negative_operands(self):
        """["-4","5","*"] -> -20"""
        for sol in self.solutions:
            self.assertEqual(-20, sol.evalRPN(["-4", "5", "*"]))

    def test_large_expression(self):
        """Multiple operations chained."""
        for sol in self.solutions:
            self.assertEqual(5, sol.evalRPN(["3", "4", "+", "2", "-"]))
