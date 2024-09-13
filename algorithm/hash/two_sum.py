"""leet code 1, easy"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_ind = dict()
        for i, n in enumerate(nums):
            v = target - n
            if v in val_ind:
                return [val_ind[v], i]
            else:
                val_ind[n] = i
