from unittest import TestCase

from algorithm.tree.add_search_word import WordDictionary, WordDictionaryMap


class TestWordDictionary(TestCase):
    def setUp(self):
        self.solutions = [WordDictionary, WordDictionaryMap]

    def test_example(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                wd = cls()
                wd.addWord("bad")
                wd.addWord("dad")
                wd.addWord("mad")
                self.assertFalse(wd.search("pad"))
                self.assertTrue(wd.search("bad"))
                self.assertTrue(wd.search(".ad"))
                self.assertTrue(wd.search("b.."))

    def test_empty_search(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                wd = cls()
                self.assertFalse(wd.search("a"))

    def test_single_char(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                wd = cls()
                wd.addWord("a")
                self.assertTrue(wd.search("a"))
                self.assertTrue(wd.search("."))
                self.assertFalse(wd.search("b"))
                self.assertFalse(wd.search(".."))

    def test_all_dots(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                wd = cls()
                wd.addWord("abc")
                wd.addWord("xyz")
                self.assertTrue(wd.search("..."))
                self.assertFalse(wd.search(".."))
                self.assertFalse(wd.search("...."))

    def test_prefix_not_word(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                wd = cls()
                wd.addWord("apple")
                self.assertFalse(wd.search("app"))
                self.assertTrue(wd.search("apple"))
                self.assertTrue(wd.search("appl."))
                self.assertTrue(wd.search(".pple"))

    def test_multiple_words_same_prefix(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                wd = cls()
                wd.addWord("app")
                wd.addWord("apple")
                self.assertTrue(wd.search("app"))
                self.assertTrue(wd.search("apple"))
                self.assertFalse(wd.search("appl"))

    def test_dot_in_middle(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                wd = cls()
                wd.addWord("bat")
                wd.addWord("bar")
                self.assertTrue(wd.search("ba."))
                self.assertTrue(wd.search("b.t"))
                self.assertTrue(wd.search("b.r"))
                self.assertFalse(wd.search("b.x"))

    def test_max_length_word(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                wd = cls()
                word = "a" * 25
                wd.addWord(word)
                self.assertTrue(wd.search(word))
                self.assertTrue(wd.search("." * 25))
                self.assertFalse(wd.search("a" * 24))
