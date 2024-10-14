"""biweekly 141, Q4"""
from functools import cache
from math import comb

mod = 10 ** 9 + 7


@cache
def f(n, k):
    if n < k: return 0
    if k == 1: return 1
    return k * (f(n - 1, k) + f(n - 1, k - 1)) % mod  # already formed k or k-1 bands


class Solution:
    """
    comb(x, i): i bands/stages choose x stages, each stage can only hold one band
    f(n, i): assign n performers to i bands, at least one performer
    pow(y,i): each band can have score from 1 to y.
    first function is comb not permute because second function is permute. band name/order does not actually add
    a permutation.
    For example,
    band1(performer 1) on stage 1, band 2(performer 2) on stage 2 is same to
    band2(performer 1) on stage 1, band 1(performer 2) on stage 2
    """

    def numberOfWays(self, n: int, x: int, y: int) -> int:
        res = 0
        for i in range(1, min(n, x) + 1):
            res += comb(x, i) * f(n, i) * pow(y, i, mod)
        return res % mod
