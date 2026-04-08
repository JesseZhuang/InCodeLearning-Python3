"""LeetCode 378 / LintCode 1272, medium."""
import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            if self._count_less_equal(matrix, mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left

    def kthSmallestHeap(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[row][0], row, 0) for row in range(min(n, k))]
        heapq.heapify(heap)

        value = matrix[0][0]
        for _ in range(k):
            value, row, col = heapq.heappop(heap)
            if col + 1 < len(matrix[row]):
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        return value

    @staticmethod
    def _count_less_equal(matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        row, col = n - 1, 0
        count = 0
        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count
