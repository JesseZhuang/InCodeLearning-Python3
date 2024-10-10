"""leet code 123"""
from typing import List

from algorithm.dp.buy_sell_stock_iv import Solution as s


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return s().maxProfit(2, prices)
