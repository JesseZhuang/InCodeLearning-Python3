"""LeetCode 115 Distinct Subsequences."""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """2D DP. dp[i][j] = number of ways to form t[0:j] from s[0:i].

        Time O(m*n), Space O(m*n) where m=len(s), n=len(t).
        """
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):  # O(m)
            dp[i][0] = 1
        for i in range(1, m + 1):  # O(m)
            for j in range(1, n + 1):  # O(n), together O(m*n)
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[m][n]


class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        """1D DP (space optimized). Traverse j in reverse to avoid overwriting.

        Time O(m*n), Space O(n).
        """
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, m + 1):  # O(m)
            for j in range(n, 0, -1):  # O(n), reverse to use previous row values
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]
