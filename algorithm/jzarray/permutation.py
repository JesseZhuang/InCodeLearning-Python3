"""leet code 46, medium"""
from typing import List


class Solution:
    """Backtracking with swap. O(n*n!) time, O(n) space."""

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(fix):  # O(n!) branches
            if fix == len(nums):
                res.append(nums.copy())  # O(n) copy
                return
            for i in range(fix, len(nums)):
                nums[i], nums[fix] = nums[fix], nums[i]
                dfs(fix + 1)
                nums[i], nums[fix] = nums[fix], nums[i]

        dfs(0)
        return res


class Solution2:
    """Iterative insertion. O(n*n!) time, O(1) space not counting result."""

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[nums[0]]]
        for i in range(1, len(nums)):  # O(n) elements to insert
            new_res = []
            for perm in res:  # O((i-1)!) existing permutations
                for j in range(i + 1):  # O(i) insertion positions
                    new_res.append(perm[:j] + [nums[i]] + perm[j:])
            res = new_res
        return res
