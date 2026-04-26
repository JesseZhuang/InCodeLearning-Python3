"""LeetCode 72 Edit Distance"""


class Solution:
    """Bottom-up DP with 1D array. O(mn) time, O(n) space."""

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))  # O(n) space: base case dp[j] = j
        for i in range(1, m + 1):  # O(m) rows
            prev = dp[0]
            dp[0] = i
            for j in range(1, n + 1):  # O(n) cols
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(prev, dp[j], dp[j - 1])  # replace, delete, insert
                prev = temp
        return dp[n]


class Solution2:
    """Bottom-up DP with 2D array. O(mn) time, O(mn) space."""

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # O(mn) space
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):  # O(m) rows
            for j in range(1, n + 1):  # O(n) cols
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],  # replace
                        dp[i - 1][j],  # delete
                        dp[i][j - 1],  # insert
                    )
        return dp[m][n]
