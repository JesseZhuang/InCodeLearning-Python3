"""LeetCode 3254, medium, tags: array, sliding window."""
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """O(n) time, O(1) space."""
        if k == 1:
            return nums
        n = len(nums)
        res = [-1] * (n - k + 1)
        streak = 1
        for i in range(n - 1):
            if nums[i] + 1 == nums[i + 1]:
                streak += 1
            else:
                streak = 1
            if streak >= k:
                res[i - k + 2] = nums[i + 1]
        return res
