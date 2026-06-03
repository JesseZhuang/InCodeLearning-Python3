"""LeetCode 312 Burst Balloons, hard."""


class Solution:
    """Interval DP (bottom-up). O(n^3) time, O(n^2) space."""

    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]  # O(n) space for padded array
        dp = [[0] * (n + 2) for _ in range(n + 2)]  # O(n^2) space
        for length in range(2, n + 2):  # O(n) lengths
            for i in range(0, n + 2 - length):  # O(n) left endpoints
                j = i + length
                for k in range(i + 1, j):  # O(n) last balloon to burst
                    coins = val[i] * val[k] * val[j] + dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], coins)
        return dp[0][n + 1]


class Solution2:
    """Interval DP (top-down with memoization). O(n^3) time, O(n^2) space."""

    def maxCoins(self, nums: list[int]) -> int:
        val = [1] + nums + [1]
        n = len(val)
        memo = {}

        def dp(left: int, right: int) -> int:
            if right - left < 2:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            res = 0
            for k in range(left + 1, right):  # O(n) choices for last burst
                coins = val[left] * val[k] * val[right] + dp(left, k) + dp(k, right)
                res = max(res, coins)
            memo[(left, right)] = res
            return res

        return dp(0, n - 1)
