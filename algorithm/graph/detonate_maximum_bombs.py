"""leet code 2101, medium, tags: array, math, depth-first search, breadth-first search, graph."""
from collections import defaultdict, deque
from typing import List


class Solution:
    """BFS from each bomb on directed graph. O(n^3) time, O(n^2) space."""

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = defaultdict(list)
        for i in range(n):  # O(n^2) build directed graph
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= ri ** 2:  # i can reach j
                    adj[i].append(j)
        res = 0
        for start in range(n):  # O(n) starts, each BFS O(n+E) where E<=n^2
            visited = {start}
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
            res = max(res, len(visited))
        return res


class Solution2:
    """DFS from each bomb on directed graph. O(n^3) time, O(n^2) space."""

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = defaultdict(list)
        for i in range(n):  # O(n^2) build directed graph
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= ri ** 2:
                    adj[i].append(j)
        res = 0
        for start in range(n):  # O(n) starts
            visited = {start}
            stack = [start]
            while stack:  # DFS O(n+E)
                u = stack.pop()
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)
            res = max(res, len(visited))
        return res
