import unittest

from algorithm.heap.last_stone_weight import Solution, Solution2


class TestLastStoneWeight(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, stones, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.lastStoneWeight(list(stones)))

    def test_example1(self):
        self.verify([2, 7, 4, 1, 8, 1], 1)

    def test_example2(self):
        self.verify([1], 1)

    def test_two_equal(self):
        self.verify([3, 3], 0)

    def test_two_different(self):
        self.verify([3, 7], 4)

    def test_all_same(self):
        self.verify([5, 5, 5, 5], 0)

    def test_all_same_odd(self):
        self.verify([5, 5, 5], 5)

    def test_descending(self):
        self.verify([10, 4, 2, 10], 2)

    def test_single_stone(self):
        self.verify([42], 42)

    def test_large_values(self):
        self.verify([1000, 999], 1)

    def test_one_dominates(self):
        self.verify([100, 1, 1, 1, 1], 96)
