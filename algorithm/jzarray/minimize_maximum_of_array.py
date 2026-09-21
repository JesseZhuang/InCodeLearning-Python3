"""LeetCode 2439 Minimize Maximum of Array"""

from math import ceil


class Solution:
    """Prefix sum greedy. O(n) time, O(1) space.

    The answer is max(ceil(prefix_sum / (i+1))) for i in [0, n).
    We can redistribute leftward but not rightward, so the bottleneck
    is the prefix that has the highest required average.
    """

    def minimizeArrayValue(self, nums: list[int]) -> int:
        res, prefix = 0, 0
        for i, v in enumerate(nums):
            prefix += v
            # ceil(prefix / (i + 1))
            res = max(res, (prefix + i) // (i + 1))
        return res


class Solution2:
    """Binary search on the answer. O(n log(max)) time, O(1) space."""

    def minimizeArrayValue(self, nums: list[int]) -> int:
        lo, hi = 0, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            # greedily check: can we make max <= mid?
            # excess from left elements can absorb deficit on the right
            excess = 0  # O(n) scan
            feasible = True
            for v in nums:
                excess += mid - v
                if excess < 0:
                    feasible = False
                    break
            if feasible:
                hi = mid
            else:
                lo = mid + 1
        return lo
