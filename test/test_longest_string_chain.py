import unittest

from algorithm.dp.longest_string_chain import Solution


class TestLongestStringChain(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        words = ["a", "b", "ba", "bca", "bda", "bdca"]
        for sol in self.solutions:
            self.assertEqual(sol.longestStrChain(words), 4)

    def test_example2(self):
        words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
        for sol in self.solutions:
            self.assertEqual(sol.longestStrChain(words), 5)

    def test_example3(self):
        words = ["abcd", "dbqca"]
        for sol in self.solutions:
            self.assertEqual(sol.longestStrChain(words), 1)

    def test_single_word(self):
        words = ["a"]
        for sol in self.solutions:
            self.assertEqual(sol.longestStrChain(words), 1)

    def test_no_chain(self):
        words = ["abc", "def", "ghi"]
        for sol in self.solutions:
            self.assertEqual(sol.longestStrChain(words), 1)

    def test_all_same_length(self):
        words = ["ab", "cd", "ef"]
        for sol in self.solutions:
            self.assertEqual(sol.longestStrChain(words), 1)

    def test_long_chain(self):
        words = ["a", "ab", "abc", "abcd", "abcde"]
        for sol in self.solutions:
            self.assertEqual(sol.longestStrChain(words), 5)

    def test_multiple_predecessors(self):
        words = ["a", "ba", "bca", "bda", "bdca"]
        for sol in self.solutions:
            self.assertEqual(sol.longestStrChain(words), 4)


if __name__ == "__main__":
    unittest.main()
