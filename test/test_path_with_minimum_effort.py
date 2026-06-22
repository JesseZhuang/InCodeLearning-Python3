import unittest

from algorithm.graph.path_with_minimum_effort import Solution, Solution2


class TestPathWithMinimumEffort(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, heights, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.minimumEffortPath(heights))

    def test_example1(self):
        self.verify([[1, 2, 2], [3, 8, 2], [5, 3, 5]], 2)

    def test_example2(self):
        self.verify([[1, 2, 3], [3, 8, 4], [5, 3, 5]], 1)

    def test_example3(self):
        self.verify(
            [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]], 0
        )

    def test_single_cell(self):
        self.verify([[5]], 0)

    def test_single_row(self):
        self.verify([[1, 10, 6, 7, 9, 10, 4, 9]], 9)

    def test_single_column(self):
        self.verify([[1], [10], [6], [7]], 9)

    def test_two_by_two(self):
        self.verify([[1, 100], [100, 1]], 99)


if __name__ == '__main__':
    unittest.main()
