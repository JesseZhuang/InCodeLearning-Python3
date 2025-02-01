"""leet 532, medium"""
from collections import Counter


class Solution:
    """5 ms, 19 mb"""

    def findPairs(self, nums: list[int], k: int) -> int:
        cnt = Counter(nums)
        return sum([k > 0 and c + k in cnt or k == 0 and cnt[c] > 1 for c in cnt])
