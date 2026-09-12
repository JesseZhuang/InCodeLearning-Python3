import unittest

from algorithm.stack.longest_valid_parentheses import Solution, Solution2


class TestLongestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses("(()"), 2)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses(")()())"), 4)

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses(""), 0)

    def test_all_open(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses("(((("), 0)

    def test_all_close(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses("))))"), 0)

    def test_full_match(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses("()()"), 4)

    def test_nested(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses("(())"), 4)

    def test_complex(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses("()(()"), 2)

    def test_long_valid_in_middle(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses(")(())()(()))("), 10)

    def test_single_char(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses("("), 0)
            self.assertEqual(sol.longest_valid_parentheses(")"), 0)

    def test_alternating(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses("()()()"), 6)

    def test_deep_nesting(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses("((()))"), 6)

    def test_disconnected(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_valid_parentheses("()()()("), 6)


if __name__ == '__main__':
    unittest.main()
