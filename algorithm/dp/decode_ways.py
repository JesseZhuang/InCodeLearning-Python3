"""leet code 91, medium"""


class Solution:
    """0 ms, 17.2 mb"""

    def numDecodings(self, s: str) -> int:
        dp, dp1, dp2, n = 0, 1, 0, len(s)  # init dp1 as dp[n] because i start from n-1
        for i in range(n - 1, -1, -1):
            dp = 0 if s[i] == '0' else dp1
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                dp += dp2
            dp2 = dp1  # dp[i+2] -> dp[i+1] when i-=1
            dp1 = dp  # dp[i+1] -> dp[i] when i-=1
        return dp


class Solution1:
    """0 ms, 17.52 mb"""

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '0': continue
            dp[i] = dp[i + 1]
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                dp[i] += dp[i + 2]
        return dp[0]


class Solution2:
    """TLE"""

    def numDecodings(self, s: str) -> int:

        def dfs(i):
            n = len(s)
            if i == n: return 1
            if s[i] == '0': return 0
            res = dfs(i + 1)
            if i < n - 1 and (s[i] == '1' or s[i] == '2' and s[i + 1] < '7'):
                res += dfs(i + 2)
            return res

        return dfs(0)
