"""LeetCode 2064 Minimized Maximum of Products Distributed to Any Store"""


class Solution:
    """Binary search. O(n*log(k)) time, O(1) space. k=max(quantities)."""

    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        left, right = 1, 100000
        while left < right:
            mid = (left + right) // 2
            stores_needed = sum((q + mid - 1) // mid for q in quantities)
            if stores_needed > n:
                left = mid + 1
            else:
                right = mid
        return left
