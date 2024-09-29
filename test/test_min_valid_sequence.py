from unittest import TestCase

from algorithm.dp.min_valid_sequence import Solution


class TestMinValidSeq(TestCase):

    def test(self):
        cases = [
            ["vbcca", "abc", [0, 1, 2]],
            ["bacdc", "abc", [1, 2, 4]],
            ["aaaaaa", "aaabc", []],
            ["abc", "ab", [0, 1]]
        ]
        tbt = Solution()
        for word1, word2, exp in cases:
            with self.subTest(word1 + "," + word2):
                self.assertEqual(exp, tbt.validSequence(word1, word2))
