"""leet code 539, medium"""
from math import inf
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """62ms, 19.6Mb"""
        minutes = [False] * (24 * 60)
        for t in timePoints:
            m = int(t[:2]) * 60 + int(t[3:])
            if minutes[m]: return 0
            minutes[m] = True
        prev, first, last, res = -1, -1, -1, inf
        for i in range(24 * 60):
            if minutes[i]:
                if prev != -1:
                    res = min(res, i - prev)
                if first == -1: first = i
                prev = i
                last = i

        return min(res, 24 * 60 - (last - first))
