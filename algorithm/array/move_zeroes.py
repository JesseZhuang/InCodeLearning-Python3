'''leet code 283 easy'''

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ind = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i > zero_ind:
                    nums[zero_ind] = nums[i]
                    nums[i] = 0
                zero_ind += 1
