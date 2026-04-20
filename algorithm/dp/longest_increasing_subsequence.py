"""LeetCode 300 Longest Increasing Subsequence, medium."""

import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """DP with binary search, patience sorting.

        Maintain a list `tails` where tails[i] is the smallest tail element
        for an increasing subsequence of length i+1.

        Time O(n log n), Space O(n).
        """
        tails: List[int] = []
        for num in nums:  # O(n)
            pos = bisect.bisect_left(tails, num)  # O(log n)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Classic DP. dp[i] = length of longest increasing subsequence ending at index i.

        Time O(n^2), Space O(n).
        """
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):  # O(n)
            for j in range(i):  # O(n), together O(n^2)
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
