"""LeetCode 2574 Left and Right Sum Differences."""


class Solution:
    """Compute differences in O(n) time and O(n) output space."""

    def leftRightDifference(self, nums: list[int]) -> list[int]:
        right_sum = sum(nums)
        left_sum = 0
        differences = []
        for value in nums:  # O(n) total; O(1) extra space beyond the output
            right_sum -= value
            differences.append(abs(left_sum - right_sum))
            left_sum += value
        return differences
