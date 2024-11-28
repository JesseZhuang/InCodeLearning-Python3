"""leet code 10, hard"""


class Solution:
    """40ms, 16.55mb"""

    def isMatch(self, s: str, p: str) -> bool:
        n, m = map(len, (s, p))
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = True
        for i in range(n, -1, -1):
            for j in range(m - 1, -1, -1):
                first_match = i < n and (s[i] == p[j] or p[j] == ".")
                if j + 1 < m and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or \
                               (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]
