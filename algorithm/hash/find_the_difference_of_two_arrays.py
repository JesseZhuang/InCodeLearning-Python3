"""LeetCode 2215, Find the Difference of Two Arrays."""


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """Return distinct exclusive values in O(n + m) time and space."""
        first_values = set(nums1)
        second_values = set(nums2)
        return [list(first_values - second_values), list(second_values - first_values)]
