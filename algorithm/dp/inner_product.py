"""lint 26, hard"""
from copy import copy


class Solution:
    """dp, 6583 ms, 5.34 mb"""

    def getMaxInnerProduct(self, A, B):
        n, k = map(len, (A, B))
        dp = [0] * (k + 1)
        for i in range(k + 1):
            ndp = copy(dp)
            for j in range(k - i + 1):  # 只会取 k - i 个数，这样就不用再另外判断会不会越界了
                if i - 1 >= 0:
                    ndp[j] = max(ndp[j], dp[j] + B[i + j - 1] * A[i - 1])
                if j - 1 >= 0:
                    ndp[j] = max(ndp[j], ndp[j - 1] + B[i + j - 1] * A[-j])
            dp = ndp
        return max(dp)


class Solution2:
    """dp, 7554 ms, 129.55 mb"""

    def getMaxInnerProduct(self, A, B):
        res, (n, k) = 0, map(len, (A, B))
        dp = [[0] * (k + 1) for _ in range(k + 1)]  # res for picking i from left, j from right
        for i in range(k + 1):
            for j in range(k - i + 1):  # try taking k-i from right
                if i - 1 >= 0:  # take from left
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + B[i + j - 1] * A[i - 1])
                if j - 1 >= 0:  # take from right
                    dp[i][j] = max(dp[i][j], dp[i][j - 1] + B[i + j - 1] * A[-j])
            res = max(res, dp[i][k - i])
        return res
