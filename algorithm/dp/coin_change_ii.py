"""LeetCode 518 Coin Change II"""


class Solution:
    """Bottom-up DP. O(N*M) time, O(M) space. N: len(coins), M: amount."""

    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)  # dp[i]: number of combinations for amount i
        dp[0] = 1
        for coin in coins:  # O(N) outer loop on coins to avoid counting permutations
            for i in range(coin, amount + 1):  # O(M)
                dp[i] += dp[i - coin]
        return dp[amount]


class Solution2:
    """2D DP. O(N*M) time, O(N*M) space. N: len(coins), M: amount."""

    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        # dp[i][j]: combinations using first i coins for amount j
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):  # O(N)
            dp[i][0] = 1  # one way to make amount 0: use no coins
        for i in range(1, n + 1):  # O(N)
            for j in range(1, amount + 1):  # O(M)
                dp[i][j] = dp[i - 1][j]  # skip coin i
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]  # use coin i (unbounded)
        return dp[n][amount]
