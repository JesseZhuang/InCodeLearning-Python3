import unittest

from algorithm.sliding.find_all_anagrams import Solution, Solution2


class TestFindAllAnagrams(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, s, p, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.findAnagrams(s, p))

    def test_example1(self):
        self.verify("cbaebabacd", "abc", [0, 6])

    def test_example2(self):
        self.verify("abab", "ab", [0, 1, 2])

    def test_no_match(self):
        self.verify("abcdef", "xyz", [])

    def test_p_longer_than_s(self):
        self.verify("ab", "abc", [])

    def test_single_char_match(self):
        self.verify("aaaa", "a", [0, 1, 2, 3])

    def test_entire_string(self):
        self.verify("abc", "cba", [0])

    def test_repeated_pattern(self):
        self.verify("aababaab", "aab", [0, 1, 3, 4, 5])

    def test_empty_s(self):
        self.verify("", "a", [])

    def test_same_length_no_match(self):
        self.verify("abc", "def", [])


if __name__ == '__main__':
    unittest.main()
