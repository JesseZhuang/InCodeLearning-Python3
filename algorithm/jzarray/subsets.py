"""LeetCode 78. Subsets. Medium. Tags: array, backtracking, bit manipulation."""

from typing import List


class Solution:
    """Backtracking. O(n*2^n) time, O(n) space excluding result."""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, cur):
            res.append(cur[:])  # O(n) copy
            for i in range(start, len(nums)):  # O(2^n) branches total
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()

        backtrack(0, [])
        return res


class Solution2:
    """Bit mask enumeration. O(n*2^n) time and space."""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for mask in range(1 << n):  # O(2^n) masks
            subset = []
            for i in range(n):  # O(n) per mask
                if mask & (1 << i):
                    subset.append(nums[i])
            res.append(subset)
        return res
