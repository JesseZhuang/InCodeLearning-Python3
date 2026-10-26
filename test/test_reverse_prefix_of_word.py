import unittest

from algorithm.jzstring.reverse_prefix_of_word import Solution


class TestReversePrefixOfWord(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example_with_multiple_occurrences(self):
        for solution in self.solutions:
            self.assertEqual("dcbaefd", solution.reversePrefix("abcdefd", "d"))

    def test_example_without_target(self):
        for solution in self.solutions:
            self.assertEqual("abcd", solution.reversePrefix("abcd", "z"))

    def test_first_character(self):
        for solution in self.solutions:
            self.assertEqual("abca", solution.reversePrefix("abca", "a"))

    def test_last_character(self):
        for solution in self.solutions:
            self.assertEqual("edcba", solution.reversePrefix("abcde", "e"))

    def test_single_character(self):
        for solution in self.solutions:
            self.assertEqual("a", solution.reversePrefix("a", "a"))
            self.assertEqual("a", solution.reversePrefix("a", "z"))

    def test_first_of_repeated_targets(self):
        for solution in self.solutions:
            self.assertEqual("baab", solution.reversePrefix("abab", "b"))

    def test_maximum_length(self):
        for solution in self.solutions:
            self.assertEqual(
                "z" + "a" * 249,
                solution.reversePrefix("a" * 249 + "z", "z"),
            )


if __name__ == "__main__":
    unittest.main()
