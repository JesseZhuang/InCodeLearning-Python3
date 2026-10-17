from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = 0
        current_run = 0
        longest = 0

        for number in nums:  # O(n) time; O(1) extra space.
            if number > maximum:
                maximum = number
                current_run = 1
                longest = 1
            elif number == maximum:
                current_run += 1
                longest = max(longest, current_run)
            else:
                current_run = 0

        return longest
