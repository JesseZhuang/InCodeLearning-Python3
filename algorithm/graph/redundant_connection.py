"""LeetCode 684, medium, tags: tree, union find, graph."""

from typing import List


class Solution:
    """Union Find. O(n * alpha(n)) time ~= O(n), O(n) space."""

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x, y) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False  # already connected — this edge is redundant
            if rank[px] < rank[py]:  # union by rank
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []


class Solution2:
    """DFS cycle detection. O(n) time, O(n) space."""

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        visited = [False] * n
        parent = [-1] * n
        cycle_start = -1

        def dfs(src):
            nonlocal cycle_start
            visited[src] = True
            for nei in adj[src]:
                if not visited[nei]:
                    parent[nei] = src
                    dfs(nei)
                elif nei != parent[src] and cycle_start == -1:
                    cycle_start = nei
                    parent[nei] = src

        dfs(0)

        cycle_nodes = set()
        node = cycle_start
        while True:
            cycle_nodes.add(node)
            node = parent[node]
            if node == cycle_start:
                break

        for i in range(len(edges) - 1, -1, -1):
            if (edges[i][0] - 1) in cycle_nodes and (edges[i][1] - 1) in cycle_nodes:
                return edges[i]
        return []
