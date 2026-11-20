"""Tests for LeetCode 3042."""
import unittest

from algorithm.jzstring.count_prefix_suffix_pairs_i import Solution


class TestCountPrefixSuffixPairsI(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_examples(self):
        cases = [
            (["a", "aba", "ababa", "aa"], 4),
            (["pa", "papa", "ma", "mama"], 2),
            (["abab", "ab"], 0),
        ]
        for solution in self.solutions:
            for words, expected in cases:
                with self.subTest(words=words):
                    self.assertEqual(expected, solution.countPrefixSuffixPairs(words))

    def test_single_word_and_order(self):
        for solution in self.solutions:
            self.assertEqual(0, solution.countPrefixSuffixPairs(["a"]))
            self.assertEqual(0, solution.countPrefixSuffixPairs(["abc", "a"]))

    def test_both_prefix_and_suffix_are_required(self):
        for solution in self.solutions:
            self.assertEqual(0, solution.countPrefixSuffixPairs(["ab", "abc"]))
            self.assertEqual(0, solution.countPrefixSuffixPairs(["bc", "abc"]))
            self.assertEqual(1, solution.countPrefixSuffixPairs(["ab", "abxab"]))

    def test_duplicates_and_maximum_input(self):
        for solution in self.solutions:
            self.assertEqual(3, solution.countPrefixSuffixPairs(["a", "a", "a"]))
            self.assertEqual(1225, solution.countPrefixSuffixPairs(["abcdefghij"] * 50))
