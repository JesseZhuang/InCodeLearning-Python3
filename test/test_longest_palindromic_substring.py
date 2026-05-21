import unittest

from algorithm.jzstring.longest_palindromic_substring import Solution, Solution2


class TestLongestPalindromicSubstring(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            res = sol.longestPalindrome("babad")
            self.assertIn(res, ["bab", "aba"])

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestPalindrome("cbbd"), "bb")

    def test_single_char(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestPalindrome("a"), "a")

    def test_two_same_chars(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestPalindrome("aa"), "aa")

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestPalindrome("aaaa"), "aaaa")

    def test_no_palindrome_longer_than_1(self):
        for sol in self.solutions:
            self.assertEqual(len(sol.longestPalindrome("abcd")), 1)

    def test_entire_string_is_palindrome(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestPalindrome("racecar"), "racecar")

    def test_even_length_palindrome(self):
        for sol in self.solutions:
            self.assertEqual(sol.longestPalindrome("abacdfgdcaba"), "aba")

    def test_long_palindrome_in_middle(self):
        for sol in self.solutions:
            res = sol.longestPalindrome("xabcbay")
            self.assertEqual(res, "abcba")


if __name__ == '__main__':
    unittest.main()
