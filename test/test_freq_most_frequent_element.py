import unittest

from algorithm.sliding.freq_most_frequent_element import Solution, Solution2


class TestFreqMostFrequentElement(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.maxFrequency([1, 2, 4], 5))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.maxFrequency([1, 4, 8, 13], 5))

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.maxFrequency([3, 9, 6], 2))

    def test_single_element(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.maxFrequency([10], 0))

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(4, sol.maxFrequency([5, 5, 5, 5], 0))

    def test_k_zero(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.maxFrequency([1, 1, 3, 3, 5], 0))

    def test_large_k(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.maxFrequency([1, 2, 3, 4, 5], 100))

    def test_consecutive(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.maxFrequency([1, 2, 3], 3))

    def test_duplicates_with_gap(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.maxFrequency([1, 1, 1, 10], 9))

    def test_large_values(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.maxFrequency([100000, 100000], 0))


if __name__ == '__main__':
    unittest.main()
