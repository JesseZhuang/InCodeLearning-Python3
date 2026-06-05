"""LeetCode 153, medium, tags: array, binary search."""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Binary search comparing mid to right boundary.

        Complexity: Time O(log n), Space O(1).
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:  # O(log n) iterations
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


class Solution2:
    def findMin(self, nums: list[int]) -> int:
        """Binary search comparing mid to left boundary.

        Complexity: Time O(log n), Space O(1).
        """
        lo, hi = 0, len(nums) - 1
        if nums[lo] <= nums[hi]:
            return nums[lo]
        while lo < hi:  # O(log n) iterations
            mid = lo + (hi - lo) // 2
            if nums[mid] >= nums[0]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
