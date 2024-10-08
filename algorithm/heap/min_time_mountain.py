"""leet code 3296, weekly contest 416 Q2, medium"""
from heapq import heappush, heappop, heapify
from typing import List


class Solution:
    """nlgk, k"""

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        w_times = workerTimes
        pq = []
        for i, wt in enumerate(w_times):  # next total is total time for worker[i] if worked
            pq.append((wt, 1, i))  # next total, round, index
        heapify(pq)
        times = [0] * len(w_times)
        mh = mountainHeight
        while mh > 0:  # O(nlgk)
            nt, r, i = heappop(pq)
            mh -= 1
            times[i] = nt
            r += 1
            heappush(pq, (nt + w_times[i] * r, r, i))
        return max(times)  # O(k)
