"""LeetCode 1143 Longest Common Subsequence"""

import functools


class Solution:
    """Space-optimized DP. O(m*n) time, O(min(m,n)) space."""

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m < n:
            return self.longestCommonSubsequence(text2, text1)
        dp = [0] * (n + 1)
        for char1 in text1:  # O(m)
            pr, prpc = 0, 0
            for j, char2 in enumerate(text2):  # O(n)
                prpc = pr
                pr = dp[j + 1]
                dp[j + 1] = prpc + 1 if char1 == char2 else max(dp[j], pr)
        return dp[-1]


class Solution2:
    """2D DP table. O(m*n) time, O(m*n) space."""

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # O(m*n) space
        for i in range(m):  # O(m)
            for j in range(n):  # O(n)
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[m][n]
