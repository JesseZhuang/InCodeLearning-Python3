import unittest

from algorithm.binary_search.search_suggestions_system import Solution, Solution2


class TestSearchSuggestionsSystem(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        search_word = "mouse"
        expected = [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
        ]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.suggestedProducts(products[:], search_word), expected)

    def test_example2(self):
        products = ["havana"]
        search_word = "havana"
        expected = [
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
        ]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.suggestedProducts(products[:], search_word), expected)

    def test_example3(self):
        products = ["bags", "baggage", "banner", "box", "cloths"]
        search_word = "bags"
        expected = [
            ["baggage", "bags", "banner"],
            ["baggage", "bags", "banner"],
            ["baggage", "bags"],
            ["bags"],
        ]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.suggestedProducts(products[:], search_word), expected)

    def test_no_match(self):
        products = ["apple", "apricot", "banana"]
        search_word = "z"
        expected = [[]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.suggestedProducts(products[:], search_word), expected)

    def test_prefix_diverges_midway(self):
        products = ["abc", "abd", "abe", "xyz"]
        search_word = "abf"
        expected = [
            ["abc", "abd", "abe"],
            ["abc", "abd", "abe"],
            [],
        ]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.suggestedProducts(products[:], search_word), expected)

    def test_single_char_products(self):
        products = ["a", "b", "c", "d"]
        search_word = "a"
        expected = [["a"]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.suggestedProducts(products[:], search_word), expected)


if __name__ == "__main__":
    unittest.main()
