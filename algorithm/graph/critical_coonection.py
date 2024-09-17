"""leet code 1192, hard"""
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """1591ms, 65.21mb"""
        res = []
        adj, ranks = [[] for _ in range(n)], [0] * n
        for e in connections:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        def dfs(v: int, parent: int, rank: int) -> int:
            if ranks[v] != 0: return ranks[v]
            ranks[v] = rank
            for w in adj[v]:
                if w == parent: continue
                ranks[w] = dfs(w, v, rank + 1)
                ranks[v] = min(ranks[v], ranks[w])
                if rank < ranks[w]: res.append([v, w])
            return ranks[v]

        dfs(0, 0, 1)
        return res
