'''leet code 33 medium'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if (nums[mid] < nums[0]) == (target<nums[0]):  # parenthesis important
                if nums[mid]<target: l=mid+1
                elif nums[mid]==target: return mid
                else: r=mid-1  # do not forget colon
            elif target<nums[0]: l=mid+1
            else: r=mid-1
        return -1
