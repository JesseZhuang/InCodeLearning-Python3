"""leet 916, medium"""
from collections import Counter


class Solution(object):
    """526 ms, 21.3 mb"""

    def wordSubsets(self, A: list[str], B: list[str]) -> list[str]:
        cnt = Counter()
        for b in B:
            cnt |= Counter(b)
        return [a for a in A if Counter(a) >= cnt]
