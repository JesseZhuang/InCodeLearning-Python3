"""LeetCode 62, medium, tags: math, dynamic programming, combinatorics."""


class Solution:
    """O(mn) time, O(min(m,n)) space. Rolling 1D DP."""

    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            return self.uniquePaths(n, m)
        dp = [0] * (m + 1)
        dp[1] = 1
        for i in range(n):  # O(n)
            for j in range(1, m + 1):  # O(m)
                dp[j] += dp[j - 1]
        return dp[m]


class Solution2:
    """O(min(m,n)) time, O(1) space. Combinatorics: C(m+n-2, m-1)."""

    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            return self.uniquePaths(n, m)
        res, j = 1, 1
        for i in range(m + n - 2, n - 1, -1):  # O(min(m,n))
            res = res * i // j
            j += 1
        return res
