from typing import List


class Solution:
    def longest_palindrome_subseq(self, s: str) -> int:
        """2D DP. dp[i][j] = LPS length of s[i..j]."""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):  # O(n)
            dp[i][i] = 1
            for j in range(i + 1, n):  # O(n), together O(n^2)
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


class Solution2:
    def longest_palindrome_subseq(self, s: str) -> int:
        """Space-optimized 1D DP. Only keep previous row."""
        n = len(s)
        dp = [0] * n
        for i in range(n - 1, -1, -1):  # O(n)
            dp[i] = 1
            prev = 0
            for j in range(i + 1, n):  # O(n), together O(n^2)
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp
        return dp[n - 1]
