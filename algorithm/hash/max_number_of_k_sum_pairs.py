"""leet 1679, medium, tags: array, hash table, two pointers, sorting."""
from collections import Counter


class Solution:
    """Hash Map / Counter. O(n) time, O(n) space."""

    def maxOperations(self, nums: list[int], k: int) -> int:
        cnt = Counter()  # O(n) space
        res = 0
        for x in nums:  # O(n)
            if cnt[k - x] > 0:  # O(1) complement found
                res += 1
                cnt[k - x] -= 1
            else:
                cnt[x] += 1  # O(1) store for later
        return res


class Solution2:
    """Sort + Two Pointers. O(n log n) time, O(1) extra space."""

    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()  # O(n log n)
        lo, hi = 0, len(nums) - 1
        res = 0
        while lo < hi:  # O(n)
            s = nums[lo] + nums[hi]
            if s == k:
                res += 1
                lo += 1
                hi -= 1
            elif s < k:
                lo += 1
            else:
                hi -= 1
        return res
