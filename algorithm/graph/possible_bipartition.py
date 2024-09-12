"""leet code 886, medium"""
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n + 1)]
        for e in dislikes:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        colors = [0] * (n + 1)

        def dfs(v: int, color: int) -> bool:
            """return true if found odd length cycle"""
            colors[v] = color
            for w in adj[v]:
                if colors[w] == 0 and dfs(w, -color):
                    return True
                elif colors[w] == color:
                    return True
            return False

        for i in range(1, n + 1):
            if colors[i] == 0 and dfs(i, 1): return False
        return True
