"""LeetCode 1827, easy. Tags: array, greedy."""


class Solution:
    """Keep the smallest feasible value at each index. O(n) time, O(1) space."""

    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        previous = nums[0]

        for index in range(1, len(nums)):  # O(n) total, O(1) work per element.
            adjusted = max(nums[index], previous + 1)
            operations += adjusted - nums[index]
            previous = adjusted

        return operations
