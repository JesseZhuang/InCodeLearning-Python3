import unittest

from algorithm.stack.valid_parenthesis_string import Solution, Solution2


class TestValidParenthesisString(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertTrue(sol.checkValidString("()"))

    def test_example2(self):
        for sol in self.solutions:
            self.assertTrue(sol.checkValidString("(*)"))

    def test_example3(self):
        for sol in self.solutions:
            self.assertTrue(sol.checkValidString("(*))"))

    def test_empty(self):
        for sol in self.solutions:
            self.assertTrue(sol.checkValidString(""))

    def test_single_star(self):
        for sol in self.solutions:
            self.assertTrue(sol.checkValidString("*"))

    def test_all_stars(self):
        for sol in self.solutions:
            self.assertTrue(sol.checkValidString("***"))

    def test_unbalanced_close(self):
        for sol in self.solutions:
            self.assertFalse(sol.checkValidString(")("))

    def test_unbalanced_open(self):
        for sol in self.solutions:
            self.assertFalse(sol.checkValidString("(("))

    def test_star_as_empty(self):
        for sol in self.solutions:
            self.assertTrue(sol.checkValidString("(*)(*)(*)"))

    def test_complex_valid(self):
        for sol in self.solutions:
            self.assertTrue(sol.checkValidString("((**))"))

    def test_complex_invalid(self):
        s = "((("
        for sol in self.solutions:
            self.assertFalse(sol.checkValidString(s))

    def test_three_open_one_star(self):
        s = "(((*)"
        for sol in self.solutions:
            self.assertFalse(sol.checkValidString(s))

    def test_star_cannot_fix(self):
        for sol in self.solutions:
            self.assertFalse(sol.checkValidString("()))("))

    def test_long_valid(self):
        # 100 chars: constraint max length
        s = "(" * 25 + "*" * 50 + ")" * 25
        for sol in self.solutions:
            self.assertTrue(sol.checkValidString(s))


if __name__ == '__main__':
    unittest.main()
