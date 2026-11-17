class Solution:
    def maximizeGreatness(self, nums):
        """Return the maximum count of positions where a permutation wins."""
        nums.sort()  # O(n log n); Timsort uses O(n) temporary space.
        matched = 0
        for value in nums:  # O(n) total; each value is considered once.
            if value > nums[matched]:
                matched += 1
        return matched
