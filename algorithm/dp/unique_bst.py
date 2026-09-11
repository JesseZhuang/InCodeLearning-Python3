"""LeetCode 96 Unique Binary Search Trees"""


class Solution:
    """Bottom-up DP (Catalan number recurrence). O(n^2) time, O(n) space."""

    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for nodes in range(2, n + 1):  # O(n)
            for root in range(1, nodes + 1):  # O(n) — pick each node as root
                dp[nodes] += dp[root - 1] * dp[nodes - root]
        return dp[n]


class Solution2:
    """Direct Catalan number formula: C(n) = C(2n,n)/(n+1). O(n) time, O(1) space."""

    def numTrees(self, n: int) -> int:
        c = 1
        for i in range(n):  # O(n)
            c = c * 2 * (2 * i + 1) // (i + 2)
        return c
