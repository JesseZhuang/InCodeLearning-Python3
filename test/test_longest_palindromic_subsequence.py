import unittest
from algorithm.dp.longest_palindromic_subsequence import Solution, Solution2


class TestLongestPalindromicSubsequence(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_palindrome_subseq("bbbab"), 4)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_palindrome_subseq("cbbd"), 2)

    def test_single_char(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_palindrome_subseq("a"), 1)

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_palindrome_subseq("aaaa"), 4)

    def test_already_palindrome(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_palindrome_subseq("racecar"), 7)

    def test_no_repeat(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_palindrome_subseq("abcde"), 1)

    def test_two_chars_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_palindrome_subseq("aa"), 2)

    def test_two_chars_diff(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_palindrome_subseq("ab"), 1)

    def test_longer_string(self):
        for sol in self.solutions:
            self.assertEqual(sol.longest_palindrome_subseq("character"), 5)


if __name__ == "__main__":
    unittest.main()
