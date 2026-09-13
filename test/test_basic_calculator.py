import unittest

from algorithm.deq.basic_calculator import Solution, Solution2


class TestBasicCalculator(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_examples(self):
        for sol in self.solutions:
            self.assertEqual(sol.calculate("1 + 1"), 2)
            self.assertEqual(sol.calculate(" 2-1 + 2 "), 3)
            self.assertEqual(sol.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

    def test_single_number(self):
        for sol in self.solutions:
            self.assertEqual(sol.calculate("0"), 0)
            self.assertEqual(sol.calculate("2147483647"), 2147483647)
            self.assertEqual(sol.calculate("42"), 42)

    def test_unary_minus(self):
        for sol in self.solutions:
            self.assertEqual(sol.calculate("-1"), -1)
            self.assertEqual(sol.calculate("-(3+2)"), -5)
            self.assertEqual(sol.calculate("-(-1)"), 1)

    def test_nested_parentheses(self):
        for sol in self.solutions:
            self.assertEqual(sol.calculate("((1+2))"), 3)
            self.assertEqual(sol.calculate("(1+(2+(3+4)))"), 10)
            self.assertEqual(sol.calculate("(7)-(0)+(4)"), 11)

    def test_spaces(self):
        for sol in self.solutions:
            self.assertEqual(sol.calculate("  3  "), 3)
            self.assertEqual(sol.calculate(" 1 + 2 "), 3)

    def test_consecutive_ops(self):
        for sol in self.solutions:
            self.assertEqual(sol.calculate("1-1+1"), 1)
            self.assertEqual(sol.calculate("1+2-3+4-5"), -1)
            self.assertEqual(sol.calculate("10-5-3"), 2)

    def test_large_expression(self):
        for sol in self.solutions:
            self.assertEqual(sol.calculate("1+1+1+1+1+1+1+1+1+1"), 10)
            self.assertEqual(sol.calculate("(1+(4+5+2)-3)+(6+8)"), 23)


if __name__ == "__main__":
    unittest.main()
