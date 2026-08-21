"""LeetCode 240, medium, tags: binary search, array, matrix, divide and conquer.

Write an efficient algorithm that searches for a value target in an m x n integer matrix.
This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

Constraints:
m == matrix.length, n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
-10^9 <= target <= 10^9
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Staircase search from top-right corner. O(m+n) time, O(1) space."""
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1  # O(m+n) iterations at most
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False

    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        """Binary search each row. O(m log n) time, O(1) space."""
        from bisect import bisect_left
        for row in matrix:  # O(m) rows
            j = bisect_left(row, target)  # O(log n) per row
            if j < len(row) and row[j] == target:
                return True
        return False
