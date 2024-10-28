"""leet code 853, medium"""
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - p) / s for p, s in sorted(zip(position, speed))]
        cur, res = 0, 0
        for t in times[::-1]:
            if t <= cur: continue
            cur = t
            res += 1
        return res
