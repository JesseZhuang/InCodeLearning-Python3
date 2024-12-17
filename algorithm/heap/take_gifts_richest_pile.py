"""leet 2558, easy"""
import math
from heapq import heapify, heappop, heappush


class Solution:
    """8 ms, 17.72 mb"""

    def pickGifts(self, gifts, k):
        pq = [-g for g in gifts]  # max heap
        heapify(pq)
        for _ in range(k):
            cur = -heappop(pq)
            heappush(pq, -math.floor(math.sqrt(cur)))
        res = 0
        while pq:
            res -= heappop(pq)
        return res
