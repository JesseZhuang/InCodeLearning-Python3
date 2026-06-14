"""Tests for LeetCode 115 Distinct Subsequences."""

import unittest

from algorithm.dp.distinct_subsequences import Solution, Solution2


class TestDistinctSubsequences(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.numDistinct("rabbbit", "rabbit"), 3)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.numDistinct("babgbag", "bag"), 5)

    def test_no_match(self):
        for sol in self.solutions:
            self.assertEqual(sol.numDistinct("abc", "def"), 0)

    def test_empty_t(self):
        for sol in self.solutions:
            self.assertEqual(sol.numDistinct("abc", ""), 1)

    def test_empty_s(self):
        for sol in self.solutions:
            self.assertEqual(sol.numDistinct("", "a"), 0)

    def test_both_empty(self):
        for sol in self.solutions:
            self.assertEqual(sol.numDistinct("", ""), 1)

    def test_s_equals_t(self):
        for sol in self.solutions:
            self.assertEqual(sol.numDistinct("abc", "abc"), 1)

    def test_single_char_repeated(self):
        for sol in self.solutions:
            self.assertEqual(sol.numDistinct("aaa", "a"), 3)

    def test_s_shorter_than_t(self):
        for sol in self.solutions:
            self.assertEqual(sol.numDistinct("ab", "abc"), 0)

    def test_large_repeated(self):
        for sol in self.solutions:
            # C(5,3) = 10 ways to pick 3 'a's from 5
            self.assertEqual(sol.numDistinct("aaaaa", "aaa"), 10)


if __name__ == "__main__":
    unittest.main()
