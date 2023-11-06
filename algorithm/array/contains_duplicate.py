'''leet code 217'''

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''530ms, 28.18Mb'''
        nums.sort()
        for i,n in enumerate(nums):
            if i == len(nums)-1: return False
            if n == nums[i+1]: return True

    def containsDuplicate(self, nums: List[int]) -> bool:
        '''478ms, 30.78Mb'''
        s = set()
        for n in nums:
            if n in s: return True
            else: s.add(n)
