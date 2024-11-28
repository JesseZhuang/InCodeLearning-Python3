"""
kmp Knuth Morris Pratt string search
this version uses 1D DFA table
"""
from typing import List


class KMP:
    def __init__(self, needle: str) -> None:
        """needle length m, O(m) time and space"""

        def build() -> List[int]:
            m = len(needle)
            i, j = 1, 0
            table = [0] * m
            while i < m and j < m:
                if needle[i] == needle[j]:
                    j += 1
                    table[i] = j
                    i += 1
                elif j == 0:
                    i += 1
                else:
                    j = table[j - 1]
            return table

        self.table = build()
        self.needle = needle

    def search(self, haystack: str) -> int:
        table, needle = self.table, self.needle
        i, j, m = 0, 0, len(table)
        while i < len(haystack) and j < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = table[j - 1]
        if j == m:
            return i - m
        else:
            return -1
