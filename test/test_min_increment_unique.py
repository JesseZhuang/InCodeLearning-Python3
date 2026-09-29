import unittest

from algorithm.jzarray.min_increment_unique import Solution, Solution2


class TestMinIncrementUnique(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(s.minIncrementForUnique([1, 2, 2]), 1)

    def test_example2(self):
        for s in self.solutions:
            self.assertEqual(s.minIncrementForUnique([3, 2, 1, 2, 1, 7]), 6)

    def test_single_element(self):
        for s in self.solutions:
            self.assertEqual(s.minIncrementForUnique([0]), 0)

    def test_already_unique(self):
        for s in self.solutions:
            self.assertEqual(s.minIncrementForUnique([1, 2, 3, 4]), 0)

    def test_all_same(self):
        for s in self.solutions:
            self.assertEqual(s.minIncrementForUnique([0, 0, 0, 0]), 6)

    def test_two_elements_same(self):
        for s in self.solutions:
            self.assertEqual(s.minIncrementForUnique([5, 5]), 1)

    def test_all_zeroes(self):
        for s in self.solutions:
            self.assertEqual(s.minIncrementForUnique([0, 0, 0]), 3)

    def test_large_values(self):
        for s in self.solutions:
            self.assertEqual(s.minIncrementForUnique([100000, 100000]), 1)

    def test_descending(self):
        for s in self.solutions:
            self.assertEqual(s.minIncrementForUnique([5, 4, 3, 2, 1]), 0)

    def test_consecutive_duplicates(self):
        for s in self.solutions:
            self.assertEqual(s.minIncrementForUnique([1, 1, 2, 2, 3, 3]), 9)


if __name__ == "__main__":
    unittest.main()
