"""leet code 56, medium"""
from typing import List


class Solution:
    """128ms, 20.5mb"""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in intervals[1:]:
            prev = res[-1]
            if i[0] > prev[1]:
                res.append(i)
            else:
                prev[1] = max(prev[1], i[1])
        return res
