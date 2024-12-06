"""leet 53 lint 41, medium"""
from math import inf


class Solution:
    """75 ms, 31.8 mb"""

    def maxSubArray(self, nums: list[int]) -> int:
        max_here, res = 0, -inf
        for n in nums:
            max_here = max(n, max_here + n)
            res = max(res, max_here)
        return res
