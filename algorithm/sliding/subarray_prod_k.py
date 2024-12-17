"""leet 713, lint 1075, medium"""
import math


class Solution:
    """43 ms, 19.35 mb"""

    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1: return 0
        res, l, r, prod = 0, 0, 0, 1
        while r < len(nums):
            prod *= nums[r]
            r += 1
            while prod >= k:
                prod //= nums[l]
                l += 1
            res += r - l  # not r-l+1 since r incremented
        return res


class Solution2:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1: return 0
        res, lgK, n = 0, math.log(k), len(nums)
        lps = [0]
        for i in range(n):
            lps.append(lps[-1] + math.log(nums[i]))
        for i in range(n):
            lo, hi = i + 1, n + 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if lps[mid] - lps[i] < lgK - 1e-9:
                    lo = mid + 1
                else:
                    hi = mid
            res += lo - i - 1
        return res
