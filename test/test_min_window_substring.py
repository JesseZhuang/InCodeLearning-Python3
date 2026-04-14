from unittest import TestCase

from algorithm.sliding.min_window_substring import Solution


class TestSolution(TestCase):
    def test_min_window(self):
        cases = [
            ("ADOBECODEBANC", "ABC", "BANC"),
            ("a", "a", "a"),
            ("a", "aa", ""),
            ("a", "b", ""),
            ("ab", "a", "a"),
            ("ab", "b", "b"),
            ("abc", "ac", "abc"),
            ("bdab", "ab", "ab"),
            ("aaflslflsldkalskaaa", "aaa", "aaa"),
            ("cabwefgewcwaefgcf", "cae", "cwae"),
        ]
        tbt = Solution()
        for s, t, exp in cases:
            with self.subTest(s=s, t=t, exp=exp):
                self.assertEqual(tbt.minWindow(s, t), exp)
