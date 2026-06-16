import unittest

from algorithm.stack.simplify_path import Solution


class TestSimplifyPath(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_basic(self):
        for s in self.solutions:
            self.assertEqual(s.simplifyPath("/home/"), "/home")

    def test_double_dot(self):
        for s in self.solutions:
            self.assertEqual(s.simplifyPath("/../"), "/")

    def test_multiple_slashes(self):
        for s in self.solutions:
            self.assertEqual(s.simplifyPath("/home//foo/"), "/home/foo")

    def test_complex(self):
        for s in self.solutions:
            self.assertEqual(s.simplifyPath("/a/./b/../../c/"), "/c")

    def test_root(self):
        for s in self.solutions:
            self.assertEqual(s.simplifyPath("/"), "/")

    def test_deep_path(self):
        for s in self.solutions:
            self.assertEqual(s.simplifyPath("/a/b/c/d"), "/a/b/c/d")

    def test_all_dots(self):
        for s in self.solutions:
            self.assertEqual(s.simplifyPath("/..."), "/...")

    def test_double_dot_in_middle(self):
        for s in self.solutions:
            self.assertEqual(s.simplifyPath("/a/b/../c/d/../e"), "/a/c/e")

    def test_pop_beyond_root(self):
        for s in self.solutions:
            self.assertEqual(s.simplifyPath("/a/../../b"), "/b")


if __name__ == '__main__':
    unittest.main()
