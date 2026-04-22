"""test leet 2452"""
import unittest

from algorithm.jzstring.words_within_two_edits import Solution, Solution2


class TestWordsWithinTwoEdits(unittest.TestCase):
    """test words within two edits of dictionary"""

    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        queries = ["word", "note", "ants", "wood"]
        dictionary = ["wood", "joke", "moat"]
        expected = ["word", "note", "wood"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.twoEditWords(queries, dictionary))

    def test_example2(self):
        queries = ["yes"]
        dictionary = ["not"]
        expected = []
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.twoEditWords(queries, dictionary))

    def test_exact_match(self):
        queries = ["abc"]
        dictionary = ["abc"]
        expected = ["abc"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.twoEditWords(queries, dictionary))

    def test_one_edit(self):
        queries = ["abc"]
        dictionary = ["axc"]
        expected = ["abc"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.twoEditWords(queries, dictionary))

    def test_two_edits(self):
        queries = ["abc"]
        dictionary = ["xyz"]
        expected = []
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.twoEditWords(queries, dictionary))

    def test_single_char(self):
        queries = ["a", "b"]
        dictionary = ["c"]
        expected = ["a", "b"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.twoEditWords(queries, dictionary))

    def test_all_same(self):
        queries = ["aaa", "aaa"]
        dictionary = ["aaa"]
        expected = ["aaa", "aaa"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.twoEditWords(queries, dictionary))

    def test_multiple_dict_words(self):
        """query matches second dictionary word within 2 edits"""
        queries = ["abc"]
        dictionary = ["xyz", "abc"]
        expected = ["abc"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.twoEditWords(queries, dictionary))

    def test_exactly_two_edits(self):
        queries = ["ab"]
        dictionary = ["cd"]
        expected = ["ab"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.twoEditWords(queries, dictionary))

    def test_three_edits_rejected(self):
        queries = ["abc"]
        dictionary = ["def"]
        expected = []
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.twoEditWords(queries, dictionary))


if __name__ == '__main__':
    unittest.main()
