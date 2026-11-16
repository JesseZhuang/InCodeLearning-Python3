import unittest

from algorithm.sliding.substrings_all_three_chars import Solution, Solution2


class TestSubstringsAllThreeChars(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_examples(self):
        for solution in self.solutions:
            self.assertEqual(10, solution.numberOfSubstrings("abcabc"))
            self.assertEqual(3, solution.numberOfSubstrings("aaacb"))
            self.assertEqual(1, solution.numberOfSubstrings("abc"))

    def test_missing_character_returns_zero(self):
        for solution in self.solutions:
            self.assertEqual(0, solution.numberOfSubstrings("aaaa"))

    def test_overlapping_valid_substrings(self):
        for solution in self.solutions:
            self.assertEqual(6, solution.numberOfSubstrings("aabcbc"))

    def test_empty_string(self):
        for solution in self.solutions:
            self.assertEqual(0, solution.numberOfSubstrings(""))

    def test_maximum_constraint_length(self):
        s = "abc" * 16_666 + "ab"
        for solution in self.solutions:
            self.assertEqual(1_249_925_001, solution.numberOfSubstrings(s))


if __name__ == "__main__":
    unittest.main()
