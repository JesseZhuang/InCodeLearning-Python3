import unittest

from algorithm.stack.remove_duplicate_letters import Solution


class TestRemoveDuplicateLetters(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeDuplicateLetters("bcabc"), "abc")

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeDuplicateLetters("cbacdcbc"), "acdb")

    def test_single_char(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeDuplicateLetters("a"), "a")

    def test_already_unique(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeDuplicateLetters("abc"), "abc")

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeDuplicateLetters("aaaa"), "a")

    def test_reverse_order(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeDuplicateLetters("cba"), "cba")

    def test_repeated_pattern(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeDuplicateLetters("abacb"), "abc")

    def test_two_chars(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeDuplicateLetters("bab"), "ab")

    def test_longer_string(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeDuplicateLetters("ecbacba"), "eacb")

    def test_descending_with_repeat(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeDuplicateLetters("edcba"), "edcba")


if __name__ == "__main__":
    unittest.main()
