"""LeetCode 2542, medium, tags: array, greedy, sorting, heap."""

import heapq
from typing import List


class Solution:

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """Sort by nums2 descending, maintain min-heap of size k on nums1 values.
        Time O(n log n), Space O(n)."""
        pairs = sorted(zip(nums2, nums1), reverse=True)  # O(n log n)
        heap = []
        total = 0
        res = 0
        for min_val, sum_val in pairs:  # O(n)
            heapq.heappush(heap, sum_val)  # O(log k)
            total += sum_val
            if len(heap) > k:
                total -= heapq.heappop(heap)  # O(log k)
            if len(heap) == k:
                res = max(res, total * min_val)
        return res
