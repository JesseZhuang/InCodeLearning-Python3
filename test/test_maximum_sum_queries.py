import unittest

from algorithm.array.maximum_sum_queries import Solution


class TestMaximumSumQueries(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for solution in self.solutions:
            self.assertEqual(
                [6, 10, 7],
                solution.maximum_sum_queries(
                    [4, 3, 1, 2],
                    [2, 4, 9, 5],
                    [[4, 1], [1, 3], [2, 5]],
                ),
            )

    def test_example2(self):
        for solution in self.solutions:
            self.assertEqual(
                [9, 9, 9],
                solution.maximum_sum_queries(
                    [3, 2, 5],
                    [2, 3, 4],
                    [[4, 4], [3, 2], [1, 1]],
                ),
            )

    def test_no_qualifying_point(self):
        for solution in self.solutions:
            self.assertEqual(
                [-1, -1],
                solution.maximum_sum_queries(
                    [1, 4], [10, 1], [[5, 1], [1, 11]]
                ),
            )

    def test_duplicate_coordinates_and_inclusive_thresholds(self):
        for solution in self.solutions:
            self.assertEqual(
                [5, -1, 5],
                solution.maximum_sum_queries(
                    [2, 2, 2], [2, 2, 3], [[2, 2], [3, 2], [2, 3]]
                ),
            )

    def test_sum_at_integer_limit(self):
        for solution in self.solutions:
            self.assertEqual(
                [2_000_000_000],
                solution.maximum_sum_queries(
                    [1_000_000_000], [1_000_000_000], [[1_000_000_000, 1_000_000_000]]
                ),
            )


if __name__ == '__main__':
    unittest.main()
