from unittest import TestCase

from algorithm.sliding.longest_repeating_character_replacement import Solution


class TestLongestRepeatingCharacterReplacement(TestCase):
    def setUp(self):
        self.solutions = [Solution().characterReplacement,
                          Solution().characterReplacement2]

    def test_examples(self):
        cases = [
            ("ABAB", 2, 4),
            ("AABABBA", 1, 4),
        ]
        for s, k, exp in cases:
            for fn in self.solutions:
                with self.subTest(s=s, k=k, fn=fn.__name__):
                    self.assertEqual(exp, fn(s, k))

    def test_single_char(self):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(1, fn("A", 0))

    def test_all_same(self):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(4, fn("AAAA", 2))

    def test_k_zero(self):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(2, fn("AABBC", 0))

    def test_k_covers_all(self):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(5, fn("ABCDE", 4))

    def test_two_chars_alternating(self):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(5, fn("ABABAB", 2))

    def test_long_replacement_at_end(self):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(5, fn("ABCAA", 2))
