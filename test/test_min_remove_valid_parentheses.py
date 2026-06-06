import unittest

from algorithm.stack.minimum_remove_to_make_valid_parentheses import Solution, Solution2


class TestMinRemoveToMakeValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            result = sol.min_remove_to_make_valid("lee(t(c)o)de)")
            self.assertIn(result, ["lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"])

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.min_remove_to_make_valid("a)b(c)d"), "ab(c)d")

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(sol.min_remove_to_make_valid("))(("), "")

    def test_no_parens(self):
        for sol in self.solutions:
            self.assertEqual(sol.min_remove_to_make_valid("abc"), "abc")

    def test_all_valid(self):
        for sol in self.solutions:
            self.assertEqual(sol.min_remove_to_make_valid("(a(b)c)"), "(a(b)c)")

    def test_empty(self):
        for sol in self.solutions:
            self.assertEqual(sol.min_remove_to_make_valid(""), "")

    def test_only_open(self):
        for sol in self.solutions:
            self.assertEqual(sol.min_remove_to_make_valid("((("), "")

    def test_only_close(self):
        for sol in self.solutions:
            self.assertEqual(sol.min_remove_to_make_valid(")))"), "")

    def test_nested(self):
        for sol in self.solutions:
            self.assertEqual(sol.min_remove_to_make_valid("(a(b(c)))"), "(a(b(c)))")

    def test_mixed_invalid(self):
        for sol in self.solutions:
            result = sol.min_remove_to_make_valid(")(a)(")
            self.assertEqual(result, "(a)")


if __name__ == '__main__':
    unittest.main()
