"""leet code 1202, medium, tags: array, hash table, string, depth-first search, breadth-first search, union find,
sorting."""

from collections import defaultdict
from typing import List


class Solution:
    """Union-Find with path compression + union by rank. O(n*α(n) + n*log(n)) time, O(n) space."""

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        rank = [0] * n

        def find(x):  # O(α(n)) amortized
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):  # O(α(n)) amortized
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1

        for a, b in pairs:  # O(n*α(n))
            union(a, b)

        groups = defaultdict(list)
        for i in range(n):  # O(n*α(n))
            groups[find(i)].append(i)

        res = list(s)
        for indices in groups.values():
            chars = sorted(res[i] for i in indices)  # O(k*log(k)), sum of all k = n
            for i, idx in enumerate(sorted(indices)):
                res[idx] = chars[i]
        return ''.join(res)


class Solution2:
    """DFS connected components. O(n*log(n) + E) time, O(n + E) space."""

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        adj = defaultdict(list)
        for a, b in pairs:  # O(E) build adjacency list
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n
        res = list(s)

        for start in range(n):  # O(n + E) total DFS across all components
            if visited[start]:
                continue
            component = []
            stack = [start]
            while stack:
                node = stack.pop()
                if visited[node]:
                    continue
                visited[node] = True
                component.append(node)
                for nei in adj[node]:
                    if not visited[nei]:
                        stack.append(nei)
            chars = sorted(res[i] for i in component)  # O(k*log(k))
            for i, idx in enumerate(sorted(component)):
                res[idx] = chars[i]
        return ''.join(res)
