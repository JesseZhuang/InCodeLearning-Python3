import unittest

from algorithm.sliding.longest_substring_k_repeating import Solution


class TestLongestSubstringKRepeating(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.longestSubstring("aaabb", 3))
            self.assertEqual(3, sol.longestSubstring2("aaabb", 3))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.longestSubstring("ababbc", 2))
            self.assertEqual(5, sol.longestSubstring2("ababbc", 2))

    def test_single_char(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.longestSubstring("a", 1))
            self.assertEqual(1, sol.longestSubstring2("a", 1))

    def test_k_larger_than_length(self):
        for sol in self.solutions:
            self.assertEqual(0, sol.longestSubstring("abc", 4))
            self.assertEqual(0, sol.longestSubstring2("abc", 4))

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.longestSubstring("aaaaa", 2))
            self.assertEqual(5, sol.longestSubstring2("aaaaa", 2))

    def test_no_valid_substring(self):
        for sol in self.solutions:
            self.assertEqual(0, sol.longestSubstring("abcdef", 2))
            self.assertEqual(0, sol.longestSubstring2("abcdef", 2))

    def test_entire_string_valid(self):
        for sol in self.solutions:
            self.assertEqual(6, sol.longestSubstring("aabbcc", 2))
            self.assertEqual(6, sol.longestSubstring2("aabbcc", 2))

    def test_split_in_middle(self):
        """'d' has freq 1 < k=2, splits into 'aaabbb' (valid) and 'cccc' (valid)."""
        for sol in self.solutions:
            self.assertEqual(6, sol.longestSubstring("aaabbbdcccc", 2))
            self.assertEqual(6, sol.longestSubstring2("aaabbbdcccc", 2))

    def test_k_equals_1(self):
        for sol in self.solutions:
            self.assertEqual(7, sol.longestSubstring("abcdefg", 1))
            self.assertEqual(7, sol.longestSubstring2("abcdefg", 1))

    def test_repeated_pattern(self):
        for sol in self.solutions:
            self.assertEqual(8, sol.longestSubstring("ababacba", 1))
            self.assertEqual(8, sol.longestSubstring2("ababacba", 1))

    def test_java_edge_case(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.longestSubstring("cbcbbaaa", 3))
            self.assertEqual(3, sol.longestSubstring2("cbcbbaaa", 3))


if __name__ == "__main__":
    unittest.main()
