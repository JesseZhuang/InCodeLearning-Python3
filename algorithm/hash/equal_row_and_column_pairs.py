"""LeetCode 2352, medium, tags: array, hash table, matrix."""

from collections import Counter
from typing import List


class Solution:

    def equalPairs(self, grid: List[List[int]]) -> int:
        size = len(grid)
        # O(n^2) expected time and O(n^2) space for row and column signatures.
        row_counts = Counter(tuple(row) for row in grid)

        matches = 0
        for column_index in range(size):
            column = tuple(grid[row_index][column_index] for row_index in range(size))
            matches += row_counts[column]
        return matches

    def equalPairsBruteForce(self, grid: List[List[int]]) -> int:
        size = len(grid)
        matches = 0
        # O(n^3) time: compare each of the n^2 row-column pairs across n cells; O(1) extra space.
        for row_index in range(size):
            for column_index in range(size):
                for offset in range(size):
                    if grid[row_index][offset] != grid[offset][column_index]:
                        break
                else:
                    matches += 1
        return matches
