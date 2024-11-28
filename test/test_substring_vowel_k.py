import unittest

from algorithm.jzstring.substring_vowel_k_consonant_i import Solution


class TestSubstringVowel(unittest.TestCase):

    def test_solution(self):
        cases = [
            ["ieaouqqieaouqq", 1, 3],
            ["iqeaouqi", 2, 3],
            ["aeuiro", 0, 0],
            ["ieiaoud", 0, 2],
            ["cuiaeo", 0, 1]
        ]
        tbt = Solution()
        for word, k, expected in cases:
            with self.subTest(word):
                self.assertEqual(expected, tbt.countOfSubstrings(word, k))
