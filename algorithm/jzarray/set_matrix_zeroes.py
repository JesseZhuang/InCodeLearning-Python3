"""LeetCode 73, medium, tags: array, hash table, matrix."""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """O(mn) time, O(1) space. Use first row/col as markers."""
        m, n = len(matrix), len(matrix[0])
        col0 = False
        for i in range(m):  # O(m)
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, n):  # O(n)
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(m - 1, -1, -1):  # O(m)
            for j in range(n - 1, 0, -1):  # O(n)
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0:
                matrix[i][0] = 0


class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """O(mn) time, O(m+n) space. Use sets to track zero rows and cols."""
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i in range(m):  # O(m)
            for j in range(n):  # O(n)
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):  # O(m)
            for j in range(n):  # O(n)
                if i in rows or j in cols:
                    matrix[i][j] = 0
