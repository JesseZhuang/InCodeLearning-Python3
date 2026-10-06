"""LeetCode 2530, medium. Tags: array, greedy, heap (priority queue)."""

import heapq


class Solution:
    """Greedy max-heap. O(n + k log n) time and O(n) auxiliary space."""

    def maxKelements(self, nums: list[int], operations: int) -> int:
        heap = [-value for value in nums]
        heapq.heapify(heap)  # O(n) heap construction.
        score = 0

        for _ in range(operations):  # O(k) rounds, O(log n) per replacement.
            maximum = -heap[0]
            score += maximum
            heapq.heapreplace(heap, -((maximum + 2) // 3))

        return score
