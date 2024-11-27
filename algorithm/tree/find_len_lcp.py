"""leet code 3043, medium"""
from math import log10
from typing import List

from algorithm.jzstruct.trie_node import TrieNode


class Solution1:
    """908ms, 31.79mb"""

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = TrieNode()  # only need next field
        for n in arr1:
            root.insert(str(n))
        res = 0
        for n in arr2:
            res = max(res, root.lcpLen(str(n)))
        return res


class Solution2:
    """666ms, 28.46mb"""

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pre = set()
        for n in arr1:
            while n > 0 and n not in pre:
                pre.add(n)
                n //= 10
        res = 0
        for n in arr2:
            while n > 0 and n not in pre: n //= 10
            if n > 0: res = max(res, int(log10(n)) + 1)
        return res
