'''leet code 62 medium'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            return self.uniquePaths(n, m)  # note self.
        res, j = 1, 1
        for i in range(m+n-2, n-1, -1):
            res = res * i // j  # important // not /
            j += 1
        return res


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            return self.uniquePaths(n, m)
        dp = [0] * (m+1)
        dp[1] = 1
        for i in range(0, n):
            for j in range(1, m+1):
                dp[j] += dp[j-1]
        return dp[m]
