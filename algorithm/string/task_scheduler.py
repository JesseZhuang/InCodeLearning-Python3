"""leet code 621, medium"""
from collections import Counter, defaultdict
from typing import List


class Solution:
    """377ms, 16.93mb, n time"""

    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_v, max_cnt, counts = 0, 0, defaultdict(int)
        for t in tasks:
            counts[t] += 1
            if counts[t] > max_v:
                max_v = counts[t]
                max_cnt = 1
            elif counts[t] == max_v:
                max_cnt += 1
        n_gaps, gap_l = max_v - 1, n + 1
        return max(len(tasks), n_gaps * gap_l + max_cnt)


class Solution2:
    """348ms, 17mb, n+k time"""

    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)  # O(n)
        max_v, max_cnt = 0, 0
        for c in count:  # O(k)
            if count[c] > max_v:
                max_v = count[c]
                max_cnt = 1
            elif count[c] == max_v:
                max_cnt += 1
        return max(len(tasks), (max_v - 1) * (n + 1) + max_cnt)
