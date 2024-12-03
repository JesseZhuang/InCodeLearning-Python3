"""leet 50, medium, gfg"""


class Solution:
    """0 ms, 17.4 mb"""

    def myPow(self, x: float, n: int) -> float:
        if n < 0: x = 1 / x
        n, p = abs(n), 1
        while n:
            if n & 1: p *= x
            x *= x
            n >>= 1
        return p
