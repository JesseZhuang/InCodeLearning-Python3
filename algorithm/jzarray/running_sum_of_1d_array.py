"""LeetCode 1480 Running Sum of 1d Array."""


class Solution:
    """In-place prefix sums. O(n) time, O(1) auxiliary space."""

    def runningSum(self, nums: list[int]) -> list[int]:
        for index in range(1, len(nums)):  # O(n) prefix updates
            nums[index] += nums[index - 1]
        return nums
