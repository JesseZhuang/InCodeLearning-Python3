import unittest

from algorithm.jzstring.merge_strings_alternately import Solution


class TestMergeStringsAlternately(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def assert_merge(self, word1, word2, expected):
        for solution in self.solutions:
            with self.subTest(word1=word1, word2=word2):
                self.assertEqual(expected, solution.mergeAlternately(word1, word2))

    def test_alternates_equal_length_words(self):
        self.assert_merge("abc", "pqr", "apbqcr")

    def test_appends_remaining_first_word_characters(self):
        self.assert_merge("abcd", "pq", "apbqcd")

    def test_appends_remaining_second_word_characters(self):
        self.assert_merge("ab", "pqrs", "apbqrs")

    def test_merges_with_an_empty_word(self):
        self.assert_merge("", "xyz", "xyz")
        self.assert_merge("xyz", "", "xyz")


if __name__ == "__main__":
    unittest.main()
