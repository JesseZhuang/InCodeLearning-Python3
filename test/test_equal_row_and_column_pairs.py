import unittest

from algorithm.hash.equal_row_and_column_pairs import Solution


class TestEqualRowAndColumnPairs(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.cases = [
            ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
            ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3),
            ([[5]], 1),
            ([[1, 2], [3, 4]], 0),
            ([[7, 7], [7, 7]], 4),
        ]

    def test_hash_count_matches_rows_with_columns(self):
        for grid, expected in self.cases:
            with self.subTest(grid=grid):
                self.assertEqual(self.solution.equalPairs(grid), expected)

    def test_brute_force_counts_matches_with_duplicates(self):
        for grid, expected in self.cases:
            with self.subTest(grid=grid):
                self.assertEqual(self.solution.equalPairsBruteForce(grid), expected)


if __name__ == '__main__':
    unittest.main()
