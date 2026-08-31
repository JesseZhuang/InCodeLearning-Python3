"""leet 50, medium, gfg"""


class Solution:
    """iterative binary exponentiation. O(lg n) time, O(1) space."""

    def myPow(self, x: float, n: int) -> float:
        if n < 0: x = 1 / x
        n, p = abs(n), 1
        while n:  # O(lg n) iterations
            if n & 1: p *= x
            x *= x
            n >>= 1
        return p


class Solution2:
    """recursive binary exponentiation. O(lg n) time and space."""

    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return 1 / x * self.myPow(1 / x, -(n + 1))  # O(lg n) recursion depth
        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x * x, n // 2)
