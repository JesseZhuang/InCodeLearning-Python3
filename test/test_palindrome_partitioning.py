"""test LeetCode 131 Palindrome Partitioning"""
import unittest

from algorithm.dp.palindrome_partitioning import Solution, Solution2


class TestPalindromePartitioning(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            result = sol.partition("aab")
            self.assertEqual(sorted(result), sorted([["a", "a", "b"], ["aa", "b"]]))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.partition("a"), [["a"]])

    def test_single_char(self):
        for sol in self.solutions:
            self.assertEqual(sol.partition("b"), [["b"]])

    def test_all_same(self):
        for sol in self.solutions:
            result = sol.partition("aaa")
            expected = [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
            self.assertEqual(sorted(result), sorted(expected))

    def test_no_multi_char_palindrome(self):
        for sol in self.solutions:
            result = sol.partition("abc")
            self.assertEqual(result, [["a", "b", "c"]])

    def test_longer(self):
        for sol in self.solutions:
            result = sol.partition("abba")
            expected = [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]
            self.assertEqual(sorted(result), sorted(expected))

    def test_max_length_single_char(self):
        for sol in self.solutions:
            result = sol.partition("aa")
            expected = [["a", "a"], ["aa"]]
            self.assertEqual(sorted(result), sorted(expected))
