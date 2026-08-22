import unittest
from collections import Counter

from algorithm.binary_search.random_pick_with_weight import Solution, Solution2


class TestRandomPickWithWeight(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution, Solution2]

    def test_single_element(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                obj = cls([1])
                for _ in range(100):
                    self.assertEqual(obj.pickIndex(), 0)

    def test_equal_weights(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                obj = cls([1, 1, 1])
                counts = Counter(obj.pickIndex() for _ in range(3000))
                for i in range(3):
                    self.assertGreater(counts[i], 500)

    def test_skewed_weights(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                obj = cls([1, 99])
                counts = Counter(obj.pickIndex() for _ in range(10000))
                self.assertGreater(counts[1], 9000)
                self.assertLess(counts[0], 2000)

    def test_multiple_weights(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                w = [3, 14, 1, 7]
                obj = cls(w)
                counts = Counter(obj.pickIndex() for _ in range(25000))
                total = sum(w)
                for i, weight in enumerate(w):
                    expected = weight / total
                    actual = counts[i] / 25000
                    self.assertAlmostEqual(actual, expected, delta=0.03)

    def test_large_weight(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                obj = cls([1, 1000000])
                counts = Counter(obj.pickIndex() for _ in range(10000))
                self.assertGreater(counts[1], 9900)

    def test_index_range(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                obj = cls([5, 5, 5, 5])
                for _ in range(1000):
                    idx = obj.pickIndex()
                    self.assertGreaterEqual(idx, 0)
                    self.assertLessEqual(idx, 3)


if __name__ == "__main__":
    unittest.main()
