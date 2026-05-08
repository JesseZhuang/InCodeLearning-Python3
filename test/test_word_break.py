import unittest

from algorithm.dp.word_break import Solution, Solution2


class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertTrue(sol.wordBreak("leetcode", ["leet", "code"]))

    def test_example2(self):
        for sol in self.solutions:
            self.assertTrue(sol.wordBreak("applepenapple", ["apple", "pen"]))

    def test_example3(self):
        for sol in self.solutions:
            self.assertFalse(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_single_char(self):
        for sol in self.solutions:
            self.assertTrue(sol.wordBreak("a", ["a"]))
            self.assertFalse(sol.wordBreak("b", ["a"]))

    def test_whole_string_is_word(self):
        for sol in self.solutions:
            self.assertTrue(sol.wordBreak("hello", ["hello"]))

    def test_reuse_word(self):
        for sol in self.solutions:
            self.assertTrue(sol.wordBreak("aaaa", ["a", "aa"]))

    def test_no_match(self):
        for sol in self.solutions:
            self.assertFalse(sol.wordBreak("abcde", ["ab", "cd", "abc"]))

    def test_backtracking_needed(self):
        """s = 'aaaaaab', dict has 'a','aa','aaa' but no 'b' — should be False."""
        for sol in self.solutions:
            self.assertFalse(sol.wordBreak("aaaaaab", ["a", "aa", "aaa"]))

    def test_longer_word_preferred(self):
        for sol in self.solutions:
            self.assertTrue(sol.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]))


if __name__ == "__main__":
    unittest.main()
