'''leet code 55, medium'''

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach, i = 0, 0
        while i <= reach and i < len(nums):
            reach = max(reach, i+nums[i])
            if reach >= len(nums)-1:
                return True
            i += 1
        return False
