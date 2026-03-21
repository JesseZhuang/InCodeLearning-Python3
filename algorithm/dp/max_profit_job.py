"""leet code 1235, hard"""
from bisect import bisect_right
from typing import List

from sortedcontainers import SortedDict


class Solution:
    """TreeMap/SortedDict, nlgn time, n space. 794ms, 54.9mb."""

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda j: j[1])
        tm = SortedDict()  # end_time:total profit
        tm[0] = 0
        for s, e, p in jobs:
            item = tm.peekitem(tm.bisect_right(s) - 1)  # floor, max key <= s
            profit = item[1] + p
            if profit > tm.peekitem()[1]: tm[e] = profit  # max key in sorted dict
        return tm.peekitem()[1]


class Solution2:
    """DP + binary search on sorted array. nlgn time, n space."""

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        n = len(jobs)
        ends = [j[0] for j in jobs]
        dp = [0] * (n + 1)  # dp[i]: max profit considering first i jobs (1-indexed)
        for i in range(1, n + 1):
            e, s, p = jobs[i - 1]
            j = bisect_right(ends, s, 0, i - 1)  # latest end <= s, search in [0, i-1)
            dp[i] = max(dp[i - 1], dp[j] + p)
        return dp[n]
