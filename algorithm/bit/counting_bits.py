"""LeetCode 338, easy, tags: dynamic programming, bit manipulation."""


class Solution:
    def countBits(self, n: int) -> list[int]:
        """DP with bit shift. O(n) time, O(1) space."""
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)  # O(1) per element
        return res


class Solution2:
    def countBits(self, n: int) -> list[int]:
        """DP with last set bit (Brian Kernighan). O(n) time, O(1) space."""
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i & (i - 1)] + 1  # O(1) per element, i&(i-1) clears lowest set bit
        return res
