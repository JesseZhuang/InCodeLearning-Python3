"""leet code 710, hard"""
import random
from typing import List


class Solution:
    """203ms, 27.22mb"""

    def __init__(self, n: int, blacklist: List[int]):
        mapping = dict()
        for b in blacklist: mapping[b] = -1
        m = n - len(mapping)  # 2,3,5:-1; 2:6,3:4,5:-1
        for b in blacklist:
            if b >= m: continue
            while n - 1 in mapping: n -= 1
            mapping[b] = n - 1
            n -= 1
        self.mapping = mapping
        self.m = m

    def pick(self) -> int:
        p = random.randrange(self.m)
        return self.mapping.get(p, p)

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
