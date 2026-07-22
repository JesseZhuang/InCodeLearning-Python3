from collections import deque


class Solution:
    """LeetCode 310. Minimum Height Trees. Topological sort peeling leaves."""

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 2:
            return list(range(n))
        adj = [set() for _ in range(n)]  # O(n) space
        for u, v in edges:  # O(n) time, tree has n-1 edges
            adj[u].add(v)
            adj[v].add(u)
        leaves = deque(i for i in range(n) if len(adj[i]) == 1)
        remaining = n
        while remaining > 2:  # O(n) total across all iterations
            leaf_count = len(leaves)
            remaining -= leaf_count
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)
        return list(leaves)
