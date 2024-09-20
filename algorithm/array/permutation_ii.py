"""leet code 47, medium"""
from collections import Counter
from typing import List


class Solution1:
    """51ms, 16.86mb"""

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def permute(begin: int) -> None:
            if begin == len(nums):
                res.append(nums.copy())
            fixed = set()
            for i in range(begin, len(nums)):
                if nums[i] in fixed: continue
                fixed.add(nums[i])
                nums[i], nums[begin] = nums[begin], nums[i]
                permute(begin + 1)
                nums[i], nums[begin] = nums[begin], nums[i]

        permute(0)
        return res


class Solution2:
    """50ms, 17.27mb"""

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counts = Counter(nums)

        def dfs(comb: List[int]) -> None:  # note no self needed when defined inside
            if len(comb) == len(nums):
                res.append(comb.copy())
            for num in counts:
                if counts[num] == 0: continue
                comb.append(num)
                counts[num] -= 1
                dfs(comb)
                comb.pop()
                counts[num] += 1

        dfs([])  # or use deque()
        return res
