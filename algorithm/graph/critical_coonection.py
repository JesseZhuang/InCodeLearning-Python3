"""leet code 1192, hard"""
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        res = []
        adj = [[] for _ in range(n)]
        for e in connections:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        ranks = [0] * n

        def dfs(v, parent, rank):
            ranks[v] = rank
            for w in adj[v]:
                if w == parent: continue
                if ranks[w] == 0:
                    ranks[w] = dfs(w, v, rank + 1)
                ranks[v] = min(ranks[v], ranks[w])
                if rank < ranks[w]: res.append([v, w])
            return ranks[v]

        dfs(0, 0, 1)
        return res
