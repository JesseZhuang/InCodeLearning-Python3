'''leet code 213 medium'''

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def simple_rob(nums, l, r):
            did_not, robbed = 0, 0
            for i in range(l, r):
                t = did_not+nums[i]
                did_not = max(did_not, robbed)
                robbed = t
            return max(robbed, did_not)
        if len(nums) == 1:
            return nums[0]
        else:
            return max(simple_rob(nums, 0, len(nums)-1), simple_rob(nums, 1, len(nums)))
