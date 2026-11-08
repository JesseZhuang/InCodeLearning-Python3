class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        """Count exact-k odd subarrays with prefix frequencies: O(n) time, O(n) space."""
        odd_prefix = 0
        frequencies = {0: 1}  # The empty prefix lets a match start at index 0.
        count = 0
        for num in nums:  # O(n); each prefix lookup and update is O(1) on average.
            odd_prefix += num & 1
            count += frequencies.get(odd_prefix - k, 0)
            frequencies[odd_prefix] = frequencies.get(odd_prefix, 0) + 1
        return count

    def numberOfSubarraysSliding(self, nums: list[int], k: int) -> int:
        """Count exact-k odds as at_most(k) - at_most(k - 1): O(n) time, O(1) space."""

        def at_most(limit: int) -> int:
            if limit < 0:
                return 0

            left = odd_count = total = 0
            for right, num in enumerate(nums):  # O(n); each item enters the window once.
                odd_count += num & 1
                while odd_count > limit:  # Each item leaves at most once, so O(n) total.
                    odd_count -= nums[left] & 1
                    left += 1
                total += right - left + 1
            return total

        return at_most(k) - at_most(k - 1)
