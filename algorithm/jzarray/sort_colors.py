"""75. Sort Colors https://leetcode.com/problems/sort-colors/"""

from typing import List


class Solution:
    """Dutch National Flag - three-way partition."""

    def sortColors(self, nums: List[int]) -> None:
        lo, mid, hi = 0, 0, len(nums) - 1  # O(1) space
        while mid <= hi:  # O(n) time, single pass
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1


class Solution2:
    """Two-pass counting sort."""

    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]
        for n in nums:  # O(n) time first pass
            counts[n] += 1
        i = 0
        for color in range(3):  # O(n) time second pass
            for _ in range(counts[color]):
                nums[i] = color
                i += 1
