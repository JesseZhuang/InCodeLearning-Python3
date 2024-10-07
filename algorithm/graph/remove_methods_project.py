"""leet code 3310, medium, weekly 418 Q2"""
from collections import deque
from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:  # u->v invokes
            adj[u].append(v)
        removed = [False] * n
        q = deque(k)
        removed[k] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not removed[v]:
                    q.append(v)
                    removed[v] = True
        for u, v in invocations:
            if not removed[u] and removed[v]:
                return list(range(n))
        return [x for x in range(n) if not removed[x]]
