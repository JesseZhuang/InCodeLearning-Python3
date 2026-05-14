"""leet 209, medium, tags: array, binary search, sliding window, prefix sum."""
import bisect


class Solution:
    """sliding window. O(n) time, O(1) space."""

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res, l, cur = len(nums) + 1, 0, 0
        for r in range(len(nums)):  # O(n), each element visited at most twice
            cur += nums[r]
            while cur >= target:  # shrink window, amortized O(n) total
                res = min(res, r - l + 1)
                cur -= nums[l]
                l += 1
        return res if res <= len(nums) else 0


class Solution2:
    """prefix sum + binary search. O(n log n) time, O(n) space."""

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):  # O(n)
            prefix[i + 1] = prefix[i] + nums[i]
        res = n + 1
        for i in range(n):  # O(n) iterations
            need = prefix[i] + target
            j = bisect.bisect_left(prefix, need, i + 1)  # O(log n) binary search
            if j <= n:
                res = min(res, j - i)
        return res if res <= n else 0
