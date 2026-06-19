import unittest

from algorithm.heap.maximum_subsequence_score import Solution


class TestMaximumSubsequenceScore(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3), 12)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1), 30)

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxScore([1, 1, 1], [1, 1, 1], 2), 2)

    def test_k_equals_n(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxScore([2, 3, 5], [4, 2, 1], 3), 10)

    def test_single_element(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxScore([5], [6], 1), 30)

    def test_large_values(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxScore([10, 20, 30], [1, 2, 3], 2), 100)


if __name__ == '__main__':
    unittest.main()
