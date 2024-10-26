"""biweekly 142 Q2, leet code 3331"""

from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def findSubtreeSizes(self, p: List[int], s: str) -> List[int]:
        n = len(p)
        new_p = p.copy()
        g = defaultdict(list)  # graph
        for i in range(1, n):
            g[p[i]].append(i)
        last_seen = dict()  # char->val where char last seen during dfs

        def change(node: int):
            ch = s[node]
            if ch in last_seen and last_seen[ch] != new_p[node]:
                new_p[node] = last_seen[ch]
            op = last_seen.get(ch, None)
            last_seen[ch] = node
            for c in g[node]:
                change(c)
            if op is None:
                del last_seen[ch]
            else:
                last_seen[ch] = op

        change(0)
        new_g = defaultdict(list)
        for i in range(1, n):
            new_g[new_p[i]].append(i)

        @cache
        def size(node: int) -> int:
            res = 1
            for child in new_g[node]:
                res += size(child)
            return res

        return [size(i) for i in range(n)]
