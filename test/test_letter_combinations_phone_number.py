import unittest

from algorithm.jzstring.letter_combinations_phone_number import Solution, Solution2


class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, digits, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sorted(expected), sorted(sol.letterCombinations(digits)))

    def test_example1(self):
        self.verify("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    def test_example2(self):
        self.verify("", [])

    def test_example3(self):
        self.verify("2", ["a", "b", "c"])

    def test_single_digit_7(self):
        self.verify("7", ["p", "q", "r", "s"])

    def test_single_digit_9(self):
        self.verify("9", ["w", "x", "y", "z"])

    def test_three_digits(self):
        result = Solution().letterCombinations("234")
        self.assertEqual(len(result), 27)  # 3 * 3 * 3

    def test_four_digits_with_7(self):
        result = Solution().letterCombinations("7893")
        self.assertEqual(len(result), 4 * 3 * 4 * 3)  # 144

    def test_all_same_digit(self):
        self.verify("22", ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"])
