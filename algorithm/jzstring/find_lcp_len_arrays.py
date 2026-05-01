"""LeetCode 3043, medium, tags: array, hash table, trie, string."""
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """Trie approach. O(m*d1+n*d2) time, O(m*d1) space."""
        trie = {}
        for num in arr1:
            node = trie
            for c in str(num):
                if c not in node:
                    node[c] = {}
                node = node[c]
        res = 0
        for num in arr2:
            node = trie
            length = 0
            for c in str(num):
                if c not in node:
                    break
                node = node[c]
                length += 1
            res = max(res, length)
        return res


class Solution2:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """HashSet approach. O(m*d1+n*d2) time, O(m*d1) space."""
        prefixes = set()
        for val in arr1:
            while val > 0 and val not in prefixes:
                prefixes.add(val)
                val //= 10
        res = 0
        for val in arr2:
            while val > 0 and val not in prefixes:
                val //= 10
            if val > 0:
                res = max(res, len(str(val)))
        return res
