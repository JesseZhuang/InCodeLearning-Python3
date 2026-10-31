import unittest

from algorithm.stack.check_if_word_is_valid_after_substitutions import Solution


class TestCheckIfWordIsValidAfterSubstitutions(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_accepts_nested_and_concatenated_insertions(self):
        for solution in self.solutions:
            self.assertTrue(solution.isValid("aabcbc"))
            self.assertTrue(solution.isValid("abcabcababcc"))

    def test_rejects_characters_in_the_wrong_order(self):
        for solution in self.solutions:
            self.assertFalse(solution.isValid("abccba"))
            self.assertFalse(solution.isValid("cababc"))

    def test_rejects_leftover_partial_patterns(self):
        for solution in self.solutions:
            self.assertFalse(solution.isValid("ab"))
            self.assertFalse(solution.isValid("aabbcc"))


if __name__ == "__main__":
    unittest.main()
