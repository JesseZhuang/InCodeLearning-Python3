"""LeetCode 309, medium, tags: array, dynamic programming.

Constraints: 1 <= prices.length <= 5000, 0 <= prices[i] <= 1000.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """State machine DP with three states. O(n) time, O(1) space.

        States: hold (have stock), sold (just sold), rest (cooldown or idle).
        """
        hold, sold, rest = float('-inf'), 0, 0
        for p in prices:  # O(n)
            hold, sold, rest = max(hold, rest - p), hold + p, max(rest, sold)
        return max(sold, rest)


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """DP with buy/sell arrays. O(n) time, O(n) space."""
        n = len(prices)
        if n < 2:
            return 0
        buy = [0] * n  # O(n) space
        sell = [0] * n
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, buy[0] + prices[1])
        for i in range(2, n):  # O(n)
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        return sell[n - 1]
