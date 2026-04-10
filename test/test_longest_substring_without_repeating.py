from unittest import TestCase

from algorithm.sliding.longest_substring_without_repeating import Solution


class TestLongestSubstringWithoutRepeating(TestCase):
    def setUp(self):
        self.solutions = [Solution().lengthOfLongestSubstring,
                          Solution().lengthOfLongestSubstring2]

    def test_examples(self):
        cases = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
        ]
        for s, exp in cases:
            for fn in self.solutions:
                with self.subTest(s=s, fn=fn.__name__):
                    self.assertEqual(exp, fn(s))

    def test_empty(self):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(0, fn(""))

    def test_single_char(self):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(1, fn("a"))

    def test_all_unique(self):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(5, fn("abcde"))

    def test_duplicate_at_edges(self):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(3, fn("abca"))

    def test_spaces_and_special(self):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(3, fn("a b"))
                self.assertEqual(2, fn("a a"))
