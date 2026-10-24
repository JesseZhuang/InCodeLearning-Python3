"""LeetCode 2485 Find the Pivot Integer."""

from math import isqrt


class Solution:
    def pivotInteger(self, n: int) -> int:
        """Check whether the total sum is a perfect square. O(1) time and space."""
        total = n * (n + 1) // 2
        candidate = isqrt(total)
        return candidate if candidate * candidate == total else -1

    def pivotIntegerPrefixSum(self, n: int) -> int:
        """Compare inclusive sums on both sides. O(n) time, O(1) space."""
        total = n * (n + 1) // 2
        prefix = 0
        for candidate in range(1, n + 1):  # O(n) candidates, O(1) work each
            prefix += candidate
            suffix = total - prefix + candidate
            if prefix == suffix:
                return candidate
        return -1
