"""LeetCode 74, medium, tags: array, binary search, matrix."""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Treat the matrix as a flattened sorted array and binary search.
        O(log(m*n)) time, O(1) space."""
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:  # O(log(m*n))
            mid = (lo + hi) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        """Binary search row, then binary search column. O(log m + log n) time, O(1) space."""
        m, n = len(matrix), len(matrix[0])
        # binary search for the row
        lo, hi = 0, m - 1
        while lo <= hi:  # O(log m)
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                break
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            return False
        row = (lo + hi) // 2
        # binary search within the row
        lo, hi = 0, n - 1
        while lo <= hi:  # O(log n)
            mid = (lo + hi) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
