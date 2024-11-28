"""leet code 2021, lint code 3517, medium"""

from collections import defaultdict
from typing import List


class Solution:

    def brightest_position(self, lights: List[List[int]]) -> int:
        da = defaultdict(int)  # or use SortedDict
        for light in lights:
            l, r = light[0] - light[1], light[0] + light[1]
            da[l] += 1
            da[r + 1] -= 1
        res, b, mx = 0, 0, 0
        for p in sorted(da):
            b += da[p]
            if mx < b:
                mx = b
                res = p
        return res
