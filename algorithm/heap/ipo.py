"""leet 502, medium"""
from heapq import heappush, heappop


class Solution:
    """286 ms, 42.4 mb"""

    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        pq, i = [], 0
        p = sorted(zip(capital, profits))
        for _ in range(k):
            while i < len(p) and p[i][0] <= w:
                heappush(pq, -p[i][1])
                i += 1
            if pq: w -= heappop(pq)
        return w
