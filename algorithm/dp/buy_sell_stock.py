"""leet code 121, easy, tags: array, dp.

Constraints: 1 <= prices.length <= 10^5, 0 <= prices[i] <= 10^4.
"""
from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """One pass tracking min price. O(n) time, O(1) space."""
        res, min_seen = 0, inf
        for p in prices:  # O(n)
            min_seen = min(p, min_seen)
            res = max(res, p - min_seen)
        return res


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """Kadane's algorithm on daily price changes. O(n) time, O(1) space."""
        max_here = res = 0
        for i in range(1, len(prices)):  # O(n)
            max_here = max(0, max_here + prices[i] - prices[i - 1])
            res = max(res, max_here)
        return res
