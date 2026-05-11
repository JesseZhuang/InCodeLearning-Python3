"""leet 973, medium, tags: array, math, divide and conquer, geometry, sorting, heap, quickselect."""
import random
from heapq import heappush, heappop


class Solution:
    """max-heap of size k. O(n log k) time, O(k) space."""

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap: list[tuple[int, list[int]]] = []
        for p in points:  # O(n log k): iterate n points, each heap op O(log k)
            dist = p[0] * p[0] + p[1] * p[1]
            heappush(heap, (-dist, p))
            if len(heap) > k:
                heappop(heap)  # evict farthest
        return [p for _, p in heap]


class Solution2:
    """quickselect. O(n) average time, O(1) space."""

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def dist(p: list[int]) -> int:
            return p[0] * p[0] + p[1] * p[1]

        def partition(lo: int, hi: int, pivot_idx: int) -> int:
            pivot_dist = dist(points[pivot_idx])
            points[pivot_idx], points[hi] = points[hi], points[pivot_idx]
            store = lo
            for i in range(lo, hi):  # O(hi - lo)
                if dist(points[i]) < pivot_dist:
                    points[store], points[i] = points[i], points[store]
                    store += 1
            points[store], points[hi] = points[hi], points[store]
            return store

        lo, hi = 0, len(points) - 1
        while lo < hi:  # O(n) average across all iterations
            pivot_idx = random.randint(lo, hi)
            mid = partition(lo, hi, pivot_idx)
            if mid == k:
                break
            elif mid < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return points[:k]
