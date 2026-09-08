import unittest

from algorithm.heap.top_k_frequent_words import Solution, Solution2


class TestTopKFrequentWords(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        for s in self.solutions:
            with self.subTest(s=s.__class__.__name__):
                self.assertEqual(["i", "love"], s.topKFrequent(words, 2))

    def test_example2(self):
        words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
        for s in self.solutions:
            with self.subTest(s=s.__class__.__name__):
                self.assertEqual(["the", "is", "sunny", "day"], s.topKFrequent(words, 4))

    def test_single_word(self):
        for s in self.solutions:
            with self.subTest(s=s.__class__.__name__):
                self.assertEqual(["a"], s.topKFrequent(["a"], 1))

    def test_all_same_frequency(self):
        words = ["b", "c", "a"]
        for s in self.solutions:
            with self.subTest(s=s.__class__.__name__):
                self.assertEqual(["a", "b"], s.topKFrequent(words, 2))

    def test_k_equals_unique_count(self):
        words = ["a", "a", "b", "b", "c"]
        for s in self.solutions:
            with self.subTest(s=s.__class__.__name__):
                self.assertEqual(["a", "b", "c"], s.topKFrequent(words, 3))

    def test_lex_order_tiebreaker(self):
        words = ["aaa", "aa", "a"]
        for s in self.solutions:
            with self.subTest(s=s.__class__.__name__):
                self.assertEqual(["a"], s.topKFrequent(words, 1))

    def test_multiple_frequencies(self):
        words = ["a", "a", "a", "b", "b", "c", "c", "d"]
        for s in self.solutions:
            with self.subTest(s=s.__class__.__name__):
                self.assertEqual(["a", "b", "c"], s.topKFrequent(words, 3))


if __name__ == '__main__':
    unittest.main()
