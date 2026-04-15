"""LeetCode 560, medium, tags: array, hash table, prefix sum."""

from collections import defaultdict


class Solution:
    """7 ms, 19.7 mb"""

    def subarraySum(self, nums: list[int], k: int) -> int:
        cnt, prefix, res = defaultdict(int), 0, 0
        cnt[0] = 1  # empty prefix sum
        for n in nums:  # O(n)
            prefix += n  # O(1)
            res += cnt[prefix - k]  # O(1), count subarrays ending here with sum k
            cnt[prefix] += 1  # O(1)
        return res


class Solution2:
    """TLE, brute force"""

    def subarraySum(self, nums: list[int], k: int) -> int:
        res, n = 0, len(nums)
        for i in range(n):  # O(n)
            total = 0
            for j in range(i, n):  # O(n)
                total += nums[j]  # O(1), together O(n^2)
                if total == k:
                    res += 1
        return res
