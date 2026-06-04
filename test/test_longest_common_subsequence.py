from unittest import TestCase

from algorithm.dp.longest_common_subsequence import Solution, Solution2


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_longest_common_subsequence(self):
        cases = [
            ("abcde", "ace", 3),
            ("abc", "abc", 3),
            ("abc", "def", 0),
            ("bsbininm", "jmjkbkjkv", 1),
            ("a", "a", 1),
            ("a", "b", 0),
            ("oxcpqrsvwf", "shmtulqrypy", 2),
            ("abcba", "abcbcba", 5),
            ("", "abc", 0),
            ("abc", "", 0),
        ]
        for sol in self.solutions:
            for text1, text2, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, t1=text1, t2=text2):
                    self.assertEqual(sol.longestCommonSubsequence(text1, text2), exp)
