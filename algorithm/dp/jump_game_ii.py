"""leet code 45, medium"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        i, p, reach, res = 0, 0, 0, 0
        while p < len(nums) - 1:
            reach = max(reach, i + nums[i])
            if i == p:
                p = reach
                res += 1
            i += 1
        return res
