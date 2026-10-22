import unittest

from algorithm.hash.determine_if_two_strings_are_close import Solution


class TestDetermineIfTwoStringsAreClose(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def verify(self, word1, word2, expected):
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__, word1=word1, word2=word2):
                self.assertEqual(solution.closeStrings(word1, word2), expected)

    def test_examples(self):
        self.verify('abc', 'bca', True)
        self.verify('a', 'aa', False)
        self.verify('cabbba', 'abbccc', True)

    def test_single_character_and_identical_words(self):
        self.verify('a', 'a', True)
        self.verify('z', 'a', False)
        self.verify('aabb', 'aabb', True)

    def test_disjoint_character_sets(self):
        self.verify('ab', 'cd', False)

    def test_partially_overlapping_character_sets(self):
        self.verify('abc', 'abd', False)

    def test_different_frequency_multisets(self):
        self.verify('aaabbc', 'aabbcc', False)

    def test_frequency_swap(self):
        self.verify('aaabbc', 'aabbbc', True)

    def test_maximum_length(self):
        self.verify('a' * 50000 + 'b' * 50000, 'b' * 50000 + 'a' * 50000, True)
        self.verify('a' * 100000, 'b' * 100000, False)


if __name__ == '__main__':
    unittest.main()
