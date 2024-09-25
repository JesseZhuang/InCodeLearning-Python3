"""leet code 582, lint code 872, medium"""
from collections import defaultdict
from typing import List


class Solution:
    """123ms, 9.81mb"""

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        def dfs(i: int):
            res.append(i)
            for c in g[i]:
                dfs(c)

        g = defaultdict(list)
        for c, p in zip(pid, ppid):
            g[p].append(c)
        res = []
        dfs(kill)
        return res
