"""leet 1400, medium"""
from collections import Counter


class Solution:
    """30 ms, 18.26 mb"""

    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        if len(s) == k: return True
        cnt = Counter(s)

        return sum([1 if cnt[c] & 1 else 0 for c in cnt]) <= k
