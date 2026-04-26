"""leet 128, medium, tags: array, hash table, union find."""
from typing import List


class Solution:
    """HashSet. Time O(n), Space O(n)."""

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # O(n)
        res = 0
        for n in num_set:  # O(n) total, inner while visits each element at most once
            if n - 1 not in num_set:
                cur = n
                length = 1
                while cur + 1 in num_set:  # O(consecutive length)
                    cur += 1
                    length += 1
                res = max(res, length)
        return res


class Solution2:
    """Union Find. Time O(n * α(n)) ≈ O(n), Space O(n)."""

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        parent = {}
        size = {}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]

        for n in nums:  # O(n)
            if n in parent:
                continue
            parent[n] = n
            size[n] = 1
            if n - 1 in parent:
                union(n, n - 1)
            if n + 1 in parent:
                union(n, n + 1)
        return max(size[find(x)] for x in parent)  # O(n)
