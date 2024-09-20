"""leet code 2050, hard"""
from collections import deque
from functools import cache
from typing import List


class SolutionDfs:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n + 1)]
        for e in relations: adj[e[0]].append(e[1])

        @cache
        def dfs(v: int) -> int:
            t = 0
            for w in adj[v]:
                t = max(t, dfs(w))
            return t + time[v - 1]

        res = 0
        for i in range(1, n + 1):
            res = max(res, dfs(i))
        return res


class SolutionBfs:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """1282ms, 45.8mb"""
        adj = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        for e in relations:
            adj[e[0]].append(e[1])
            indegree[e[1]] += 1
        q = deque()
        max_time = [0] * (n + 1)
        for v in range(1, n + 1):
            if indegree[v] == 0:
                q.append(v)
                max_time[v] = time[v - 1]
        while q:
            v = q.popleft()
            for w in adj[v]:
                max_time[w] = max(max_time[w], max_time[v] + time[w - 1])
                indegree[w] -= 1
                if indegree[w] == 0:
                    q.append(w)
        return max(max_time)
