"""LeetCode 97 Interleaving String"""


class Solution:
    """Bottom-up DP with 1D array. O(mn) time, O(n) space."""

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [False] * (n + 1)
        for i in range(m + 1):  # O(m) rows
            for j in range(n + 1):  # O(n) cols
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i - 1]
                else:
                    dp[j] = (
                        (dp[j] and s1[i - 1] == s3[i + j - 1])
                        or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                    )
        return dp[n]


class Solution2:
    """Bottom-up DP with 2D array. O(mn) time, O(mn) space."""

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]  # O(mn) space
        dp[0][0] = True
        for i in range(1, m + 1):  # O(m) first column
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):  # O(n) first row
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, m + 1):  # O(m) rows
            for j in range(1, n + 1):  # O(n) cols
                dp[i][j] = (
                    (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                    or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
                )
        return dp[m][n]
