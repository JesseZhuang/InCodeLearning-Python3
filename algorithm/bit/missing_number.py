'''leet code 268 easy'''

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''128ms, 17.7Mb'''
        res = len(nums)
        for i, n in enumerate(nums):
            res = res ^ i ^ n
        return res

    def missingNumber2(self, nums: List[int]) -> int:
        '''96ms, 17.8Mb'''
        n = len(nums)
        sum = (0+n)*(n+1)//2
        for n in nums:
            sum -= n
        return sum
