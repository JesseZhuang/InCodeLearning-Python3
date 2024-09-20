"""leet code 1235, hard"""
from typing import List

from sortedcontainers import SortedDict


class Solution:
    """794ms, 54.9mb"""

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        dp = sorted(jobs, key=lambda j: j[1])
        tm = SortedDict()  # end_time:total profit
        tm[0] = 0
        for s, e, p in dp:  # start, end, profit
            item = tm.peekitem(tm.bisect_right(s) - 1)  # floor, max key <= s
            profit = item[1] + p
            if profit > tm.peekitem()[1]: tm[e] = profit  # max key in sorted dict
        return tm.peekitem()[1]
