"""LeetCode 1493, medium, tags: array, sliding window, prefix sum."""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """Sliding window, O(n) time and O(1) extra space."""
        left = zeros = best = 0
        for right, value in enumerate(nums):  # O(n): each right endpoint is visited once.
            if value == 0:
                zeros += 1
            while zeros > 1:  # O(n) amortized: left advances at most n times overall.
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left)
        return best


class Solution2:
    def longestSubarray(self, nums: list[int]) -> int:
        """Prefix/suffix counts, O(n) time and O(n) extra space."""
        n = len(nums)
        ones_before = [0] * n
        ones_after = [0] * n

        consecutive_ones = 0
        for index, value in enumerate(nums):  # O(n): count ones strictly before each index.
            ones_before[index] = consecutive_ones
            consecutive_ones = consecutive_ones + 1 if value == 1 else 0

        consecutive_ones = 0
        for index in range(n - 1, -1, -1):  # O(n): count ones strictly after each index.
            ones_after[index] = consecutive_ones
            consecutive_ones = consecutive_ones + 1 if nums[index] == 1 else 0

        best = 0
        for index in range(n):  # O(n): delete this index and join its adjacent runs.
            best = max(best, ones_before[index] + ones_after[index])
        return best
