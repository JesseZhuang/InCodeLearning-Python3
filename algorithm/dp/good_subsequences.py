"""leet 2539, lint 3855, medium"""
from collections import Counter

N = 10001
MOD = 10 ** 9 + 7
f = [1] * N
g = [1] * N
for i in range(1, N):
    f[i] = f[i - 1] * i % MOD
    g[i] = pow(f[i], MOD - 2, MOD)


def comb(n, k):
    return f[n] * g[k] * g[n - k] % MOD


class Solution:
    """todo editorial"""

    def countGoodSubsequences(self, s: str) -> int:
        cnt = Counter(s)
        res = 0
        for i in range(1, max(cnt.values()) + 1):
            x = 1
            for v in cnt.values():
                if v >= i:
                    x = x * (comb(v, i) + 1) % MOD
            res = (res + x - 1) % MOD
        return res
