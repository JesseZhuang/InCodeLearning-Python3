"""leet 2466, lint 3854, medium"""


class Solution:
    """87 ms, 22.22 mb"""

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp, mod = [1] + [0] * high, 10 ** 9 + 7  # res with length i
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]  # appending zero '0' on top of dp[i-zero]
            if i >= one:
                dp[i] += dp[i - one]  # appending one '1' on top of dp[i-one]
            dp[i] %= mod
        return sum(dp[low: high + 1]) % mod
