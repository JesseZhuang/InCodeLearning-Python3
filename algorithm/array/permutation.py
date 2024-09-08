"""leet code 46, medium"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, res)
        return res

    def dfs(self, nums: List[int], begin: int, res: List[List[int]]) -> None:
        if begin == len(nums):
            res.append(nums.copy())
            return
        for i in range(begin, len(nums)):
            nums[i], nums[begin] = nums[begin], nums[i]
            self.dfs(nums, begin + 1, res)
            nums[i], nums[begin] = nums[begin], nums[i]
