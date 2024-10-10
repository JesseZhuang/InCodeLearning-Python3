"""leet code 962, medium"""
from collections import deque
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        s = deque()
        for i, n in enumerate(nums):
            if not s or nums[s[-1]] > n: s.append(i)
        res = 0
        for j in range(len(nums) - 1, -1, -1):
            while s and nums[s[-1]] <= nums[j]:
                res = max(res, j - s[-1])
                s.pop()
        return res
