"""leet code 710, hard"""
import random
from typing import List


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.mapping = dict()
        for b in blacklist: self.mapping[b] = -1
        self.m = n - len(self.mapping)  # 2,3,5:-1; 2:6,3:4,5:-1
        for b in blacklist:
            if b >= self.m: continue
            while n - 1 in self.mapping: n -= 1
            self.mapping[b] = n - 1
            n -= 1

    def pick(self) -> int:
        p = random.randrange(self.m)
        return self.mapping.get(p, p)

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
