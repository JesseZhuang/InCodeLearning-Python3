"""leet code 47, medium"""
from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counts = Counter(nums)

        def dfs(comb):  # note no self needed when defined inside
            if len(comb) == len(nums):
                res.append(comb.copy())
                return
            for num in counts:
                if counts[num] == 0: continue
                comb.append(num)
                counts[num] -= 1
                dfs(comb)
                comb.pop()
                counts[num] += 1

        dfs([])
        return res
