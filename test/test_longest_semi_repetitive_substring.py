import unittest

from algorithm.sliding.longest_semi_repetitive_substring import Solution


class TestLongestSemiRepetitiveSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(4, self.solution.longestSemiRepetitiveSubstring("52233"))
        self.assertEqual(4, self.solution.longestSemiRepetitiveSubstring("5494"))

    def test_no_adjacent_equal_digits(self):
        self.assertEqual(6, self.solution.longestSemiRepetitiveSubstring("123456"))
        self.assertEqual(2, self.solution.longestSemiRepetitiveSubstring("12"))
        self.assertEqual(1, self.solution.longestSemiRepetitiveSubstring("5"))

    def test_one_adjacent_equal_pair(self):
        self.assertEqual(6, self.solution.longestSemiRepetitiveSubstring("122345"))

    def test_multiple_pairs_and_shrinking(self):
        self.assertEqual(4, self.solution.longestSemiRepetitiveSubstring("112233"))
        self.assertEqual(5, self.solution.longestSemiRepetitiveSubstring("1233112"))

    def test_repeated_digits(self):
        self.assertEqual(2, self.solution.longestSemiRepetitiveSubstring("111111"))
        self.assertEqual(2, self.solution.longestSemiRepetitiveSubstring("11"))

    def test_pairs_at_both_ends(self):
        self.assertEqual(6, self.solution.longestSemiRepetitiveSubstring("1123455"))


if __name__ == "__main__":
    unittest.main()
