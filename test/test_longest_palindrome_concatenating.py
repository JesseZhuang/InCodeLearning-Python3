import unittest

from algorithm.hash.longest_palindrome_concatenating import Solution


class TestLongestPalindromeConcatenating(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestPalindrome(["lc", "cl", "gg"]), 6)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]), 8)

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestPalindrome(["cc", "ll", "xx"]), 2)

    def test_all_palindromic_words(self):
        for sol in self.solutions:
            # "aa" x4 => 2 pairs => 8, plus no leftover odd
            self.assertEqual(sol.longestPalindrome(["aa", "aa", "aa", "aa"]), 8)

    def test_palindromic_words_with_center(self):
        for sol in self.solutions:
            # "aa" x3 => 1 pair (4) + 1 center (2) = 6
            self.assertEqual(sol.longestPalindrome(["aa", "aa", "aa"]), 6)

    def test_no_pairs(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestPalindrome(["ab", "cd", "ef"]), 0)

    def test_single_palindromic_word(self):
        for sol in self.solutions:
            # Single "gg" can be center
            self.assertEqual(sol.longestPalindrome(["gg"]), 2)

    def test_multiple_palindromic_types_with_center(self):
        for sol in self.solutions:
            # "aa" x2 => 1 pair (4), "bb" x2 => 1 pair (4), "cc" x1 => center (2)
            self.assertEqual(
                sol.longestPalindrome(["aa", "aa", "bb", "bb", "cc"]), 10
            )

    def test_mixed(self):
        for sol in self.solutions:
            # "ab"/"ba" => 1 pair (4), "ll" x1 => center (2) = 6
            self.assertEqual(sol.longestPalindrome(["ab", "ba", "ll"]), 6)

    def test_empty(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestPalindrome([]), 0)


if __name__ == "__main__":
    unittest.main()
