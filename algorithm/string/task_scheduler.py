"""leet code 621, medium"""
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_v, max_cnt = 0, 0
        for c in count:
            if count[c] > max_v:
                max_v = count[c]
                max_cnt = 1
            elif count[c] == max_v:
                max_cnt += 1
        return max(len(tasks), (max_v - 1) * (n + 1) + max_cnt)
