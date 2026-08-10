"""LeetCode 279, medium, tags: dynamic programming, math, BFS."""
from math import isqrt


class Solution:
    """DP. O(N*sqrt(N)) time, O(N) space."""

    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for m in range(1, n + 1):  # O(N)
            dp[m] = m  # worst case: all 1s
            i = 1
            while i * i <= m:  # O(sqrt(N))
                dp[m] = min(dp[m], dp[m - i * i] + 1)
                i += 1
        return dp[n]


class Solution2:
    """Lagrange's four-square theorem + Legendre's three-square theorem.
    O(sqrt(N)) time, O(1) space."""

    def numSquares(self, n: int) -> int:
        sr = isqrt(n)
        if sr * sr == n:
            return 1
        # reduce by factor of 4
        t = n
        while t % 4 == 0:
            t //= 4
        if t % 8 == 7:
            return 4
        i = 1
        while i * i <= n:
            remainder = n - i * i
            base = isqrt(remainder)
            if base * base == remainder:
                return 2
            i += 1
        return 3
