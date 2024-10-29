"""leet code 2501, medium"""
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        uniq, res = set(nums), 0
        for n in nums:
            cnt, cur = 0, n
            while cur in uniq:
                cnt += 1
                if cur * cur > 1e5:
                    break
                cur *= cur
            res = max(res, cnt)
        return res if res >= 2 else -1
