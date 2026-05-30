import unittest

from algorithm.jzstring.palindromic_substrings import Solution1, Solution2


class TestPalindromicSubstrings(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution1(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubstrings("abc"), 3)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubstrings("aaa"), 6)

    def test_single_char(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubstrings("a"), 1)

    def test_two_same_chars(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubstrings("aa"), 3)

    def test_two_diff_chars(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubstrings("ab"), 2)

    def test_longer_palindrome(self):
        # "racecar" has: 7 single chars + "aceca" + "cec" + "racecar" = 10
        for sol in self.solutions:
            self.assertEqual(sol.countSubstrings("racecar"), 10)

    def test_all_same(self):
        # "aaaa" has: 4 + 3 + 2 + 1 = 10
        for sol in self.solutions:
            self.assertEqual(sol.countSubstrings("aaaa"), 10)

    def test_no_palindrome_longer_than_1(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubstrings("abcd"), 4)

    def test_even_palindrome(self):
        # "abba": a, b, b, a, bb, abba = 6
        for sol in self.solutions:
            self.assertEqual(sol.countSubstrings("abba"), 6)


if __name__ == '__main__':
    unittest.main()
