"""leet code 3311, hard, weekly 418 Q3"""
from typing import List


class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        count = [0] * n  # indegree
        adj = [[] for _ in range(n)]
        for u, v in edges:
            count[u] += 1
            count[v] += 1
            adj[u].append(v)
            adj[v].append(u)
        ff = count.index(min(count))
        visited = [False] * n
        visited[ff] = True
        cur = ff
        row = [cur]
        while cur == ff or count[cur] != count[ff]:
            nxt = -1
            for v in adj[cur]:
                if not visited[v] and (nxt == -1 or count[v] < count[nxt]):
                    nxt = v
            cur = nxt
            row.append(cur)
            visited[cur] = True
        res = [[0] * len(row) for _ in range(n // len(row))]
        res[0] = row
        for i in range(0, len(res) - 1):
            for j in range(len(row)):
                cur = res[i][j]
                for v in adj[cur]:
                    if not visited[v]:
                        nxt = v
                visited[nxt] = True
                res[i + 1][j] = nxt
        return res
