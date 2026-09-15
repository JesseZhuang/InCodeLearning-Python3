"""LeetCode 974, medium, tags: array, hash table, prefix sum."""

from collections import defaultdict


class Solution:
    """O(n) time, O(k) space. Prefix sum with modular arithmetic."""

    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        cnt, prefix, res = defaultdict(int), 0, 0
        cnt[0] = 1  # empty prefix
        for n in nums:  # O(n)
            prefix += n  # O(1)
            rem = prefix % k  # O(1), Python mod always non-negative for positive k
            res += cnt[rem]  # O(1), subarrays ending here with sum divisible by k
            cnt[rem] += 1  # O(1)
        return res


class Solution2:
    """O(n^2) time, O(1) space. Brute force."""

    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        res, n = 0, len(nums)
        for i in range(n):  # O(n)
            total = 0
            for j in range(i, n):  # O(n), together O(n^2)
                total += nums[j]  # O(1)
                if total % k == 0:
                    res += 1
        return res
