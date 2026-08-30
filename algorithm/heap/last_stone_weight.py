"""leet 1046, easy"""
import bisect
import heapq


class Solution:
    """Max-heap approach, O(n log n) time, O(n) space."""

    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-s for s in stones]  # O(n)
        heapq.heapify(heap)  # O(n)
        while len(heap) > 1:
            first = -heapq.heappop(heap)  # O(log n)
            second = -heapq.heappop(heap)  # O(log n)
            if first != second:
                heapq.heappush(heap, -(first - second))  # O(log n)
        return -heap[0] if heap else 0


class Solution2:
    """Sorted list with bisect insort, O(n^2) time, O(n) space."""

    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = sorted(stones)  # O(n log n)
        while len(stones) > 1:
            first = stones.pop()  # O(1), largest
            second = stones.pop()  # O(1), second largest
            if first != second:
                bisect.insort(stones, first - second)  # O(n) shift
        return stones[0] if stones else 0
