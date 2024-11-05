"""
LeetCode 3301, biweekly 140, Q2, medium.
maximumHeight[i] denotes the maximum height the ith tower can be assigned
1. no two towers have same height
2. tower height should be a positive int
return max total sum, -1 if not possible.

Constraints:
1 <= maximumHeight.length<= 10^5, n
1 <= maximumHeight[i] <= 10^9, m
"""
from math import inf
from typing import List


class Solution:
    def maximumTotalSum(self, maxH: List[int]) -> int:
        s, last = 0, inf
        maxH.sort()
        for i in reversed(maxH):
            last = min(last - 1, i)
            if last <= 0:
                return -1
            s += last
        return s
