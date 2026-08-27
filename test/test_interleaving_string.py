from unittest import TestCase

from algorithm.dp.interleaving_string import Solution, Solution2


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_is_interleave(self):
        cases = [
            ("aabcc", "dbbca", "aadbbcbcac", True),
            ("aabcc", "dbbca", "aadbbbaccc", False),
            ("", "", "", True),
            ("", "", "a", False),
            ("a", "", "a", True),
            ("", "b", "b", True),
            ("a", "b", "ab", True),
            ("a", "b", "ba", True),
            ("a", "b", "c", False),
            ("abc", "def", "adbcef", True),
            ("abc", "def", "abcdef", True),
            ("abc", "def", "defabc", True),
            ("abc", "def", "abdcfe", False),
            ("a", "", "b", False),
            ("aaaa", "aaaa", "aaaaaaaa", True),
            ("ab", "cd", "acbd", True),
            ("ab", "cd", "cadb", True),
            ("ab", "cd", "cdba", False),
        ]
        for sol in self.solutions:
            for s1, s2, s3, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, s1=s1, s2=s2, s3=s3):
                    self.assertEqual(sol.isInterleave(s1, s2, s3), exp)
