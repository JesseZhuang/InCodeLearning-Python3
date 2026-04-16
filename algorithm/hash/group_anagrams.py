"""LeetCode 49, medium, tags: array, hash table, string, sorting."""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Sort each string to form a canonical key and group by that key.

        Time O(n * k log k) where n = len(strs) and k = max string length — sorting each string.
        Space O(n * k) for storing all strings in the groups.
        """
        groups: dict[str, list[str]] = defaultdict(list)
        for s in strs:  # O(n)
            key = ''.join(sorted(s))  # O(k log k)
            groups[key].append(s)
        return list(groups.values())


class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Use character frequency count as key to avoid sorting.

        Time O(n * k) — counting characters is O(k) per string, 26 is constant.
        Space O(n * k) for storing all strings in the groups.
        """
        groups: dict[tuple, list[str]] = defaultdict(list)
        for s in strs:  # O(n)
            count = [0] * 26  # O(26) = O(1)
            for c in s:  # O(k)
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())
