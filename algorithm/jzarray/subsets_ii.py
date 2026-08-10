"""LeetCode 90. Subsets II. Medium. Tags: array, backtracking, bit manipulation."""

from typing import List


class Solution:
    """Backtracking with duplicate skipping. O(n*2^n) time, O(n) space excluding result."""

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(n log n)
        res = []

        def backtrack(start, cur):
            res.append(cur[:])  # O(n) copy
            for i in range(start, len(nums)):  # O(2^n) branches total
                if i > start and nums[i] == nums[i - 1]:  # skip duplicate at same level
                    continue
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()

        backtrack(0, [])
        return res


class Solution2:
    """Iterative cascading with duplicate handling. O(n*2^n) time and space."""

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(n log n)
        res = [[]]
        prev_size = 0
        for i in range(len(nums)):  # O(n) outer
            start = prev_size if i > 0 and nums[i] == nums[i - 1] else 0
            prev_size = len(res)
            new_subsets = []
            for j in range(start, prev_size):  # O(2^n) total across all iterations
                new_subsets.append(res[j] + [nums[i]])  # O(n) copy
            res.extend(new_subsets)
        return res
