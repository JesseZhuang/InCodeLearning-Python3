"""leet code 46, medium"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(fix):
            if fix == len(nums):
                res.append(nums.copy())
                return
            for i in range(fix, len(nums)):
                nums[i], nums[fix] = nums[fix], nums[i]
                dfs(fix + 1)
                nums[i], nums[fix] = nums[fix], nums[i]

        dfs(0)
        return res
