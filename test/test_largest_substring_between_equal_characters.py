"""Tests for LeetCode 1624: Largest Substring Between Two Equal Characters."""

import unittest

from algorithm.jzstring.largest_substring_between_equal_characters import Solution


class TestLargestSubstringBetweenEqualCharacters(unittest.TestCase):
    """Verify the distance between equal endpoint characters."""

    def setUp(self):
        self.solutions = [Solution()]

    def test_examples(self):
        cases = [("aa", 0), ("abca", 2), ("cbzxy", -1)]
        for value, expected in cases:
            for solution in self.solutions:
                with self.subTest(value=value, solution=solution.__class__.__name__):
                    self.assertEqual(expected, solution.maxLengthBetweenEqualCharacters(value))

    def test_repeated_character_uses_farthest_pair(self):
        for solution in self.solutions:
            self.assertEqual(4, solution.maxLengthBetweenEqualCharacters("cabbac"))

    def test_adjacent_pair_has_empty_substring(self):
        for solution in self.solutions:
            self.assertEqual(0, solution.maxLengthBetweenEqualCharacters("abcdd"))

    def test_no_repeated_character_returns_negative_one(self):
        for solution in self.solutions:
            self.assertEqual(-1, solution.maxLengthBetweenEqualCharacters("abcdef"))


if __name__ == "__main__":
    unittest.main()
