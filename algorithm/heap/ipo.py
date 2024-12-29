"""leet 502, medium"""
from heapq import heappush, heappop


class Solution:
    """247 ms, 43.00 mb"""

    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        pq, i = [], 0
        p = sorted(zip(capital, profits))
        for _ in range(k):
            while i < len(p) and p[i][0] <= w:
                heappush(pq, -p[i][1])
                i += 1
            if pq:
                w -= heappop(pq)
            else:  # stuck, no more projects with capital <= w
                break
        return w
