"""LeetCode 2462, medium. Tags: array, two pointers, heap (priority queue), simulation."""
import heapq
from typing import List


class Solution:
    """Two min-heaps for front and back candidates. O(k log candidates) time, O(candidates) space."""

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        front = []  # min-heap for first `candidates` elements
        back = []  # min-heap for last `candidates` elements
        lo, hi = 0, n - 1

        # O(candidates) - initialize both heaps
        for _ in range(candidates):
            if lo <= hi:
                heapq.heappush(front, (costs[lo], lo))
                lo += 1
        for _ in range(candidates):
            if lo <= hi:
                heapq.heappush(back, (costs[hi], hi))
                hi -= 1

        total = 0
        for _ in range(k):  # O(k) iterations, each O(log candidates)
            if not back or (front and front[0] <= back[0]):
                cost, _ = heapq.heappop(front)
                total += cost
                if lo <= hi:
                    heapq.heappush(front, (costs[lo], lo))
                    lo += 1
            else:
                cost, _ = heapq.heappop(back)
                total += cost
                if lo <= hi:
                    heapq.heappush(back, (costs[hi], hi))
                    hi -= 1
        return total


class Solution2:
    """Single min-heap with index tracking. O((candidates + k) log(candidates)) time, O(candidates) space."""

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        heap = []
        lo, hi = 0, n - 1

        # O(candidates) - push from both ends
        for _ in range(candidates):
            if lo <= hi:
                heapq.heappush(heap, (costs[lo], lo, 0))  # 0 = front
                lo += 1
        for _ in range(candidates):
            if lo <= hi:
                heapq.heappush(heap, (costs[hi], hi, 1))  # 1 = back
                hi -= 1

        total = 0
        for _ in range(k):  # O(k log candidates)
            cost, idx, side = heapq.heappop(heap)
            total += cost
            if lo <= hi:
                if side == 0:
                    heapq.heappush(heap, (costs[lo], lo, 0))
                    lo += 1
                else:
                    heapq.heappush(heap, (costs[hi], hi, 1))
                    hi -= 1
        return total
