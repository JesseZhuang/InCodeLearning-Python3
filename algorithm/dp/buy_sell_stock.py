"""leet code 121, easy"""
from math import inf
from typing import List


class Solution:
    """776ms,27.4mb"""

    def maxProfit(self, prices: List[int]) -> int:
        res, min_seen = 0, inf  # res: max_here max profit sold at that index
        for p in prices:
            min_seen = min(p, min_seen)
            res = max(res, p - min_seen)
        return res
