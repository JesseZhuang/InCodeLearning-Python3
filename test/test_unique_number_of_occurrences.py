import unittest

from algorithm.hash.unique_number_of_occurrences import Solution


class TestUniqueNumberOfOccurrences(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            Solution().uniqueOccurrences,
            Solution().uniqueOccurrencesByFrequencyArray,
        ]

    def test_example_one(self):
        for solution in self.solutions:
            self.assertTrue(solution([1, 2, 2, 1, 1, 3]))

    def test_example_two(self):
        for solution in self.solutions:
            self.assertFalse(solution([1, 2]))

    def test_example_three(self):
        for solution in self.solutions:
            self.assertTrue(solution([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))

    def test_single_value(self):
        for solution in self.solutions:
            self.assertTrue(solution([42]))

    def test_equal_values(self):
        for solution in self.solutions:
            self.assertTrue(solution([7, 7, 7]))

    def test_two_values_with_equal_frequencies(self):
        for solution in self.solutions:
            self.assertFalse(solution([1, 1, 2, 2, 3, 3]))

    def test_value_bounds(self):
        for solution in self.solutions:
            self.assertTrue(solution([-1000, -1000, 1000]))
            self.assertFalse(solution([-1000, -1000, 1000, 1000, 0, 0]))


if __name__ == '__main__':
    unittest.main()
