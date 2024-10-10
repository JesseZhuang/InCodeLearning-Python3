"""leet code 188, hard"""
from typing import List

from algorithm.util.constants import INT_MIN


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n, res = len(prices), 0
        if k >= n // 2:
            for i in range(1, n):
                if prices[i] > prices[i - 1]: res += prices[i] - prices[i - 1]
            return res
        buy, sell = [INT_MIN] * (k + 1), [0] * (k + 1)  # max when bought/sold k times

        for p in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - p)
                sell[j] = max(sell[j], buy[j] + p)
        return sell[k]
