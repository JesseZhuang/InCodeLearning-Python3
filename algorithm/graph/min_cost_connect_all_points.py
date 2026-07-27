"""leet code 1584, medium, tags: array, union find, graph, minimum spanning tree."""

import heapq
from typing import List


class Solution:
    """Prim's algorithm with min-heap. O(n^2 * log(n)) time, O(n^2) space."""

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        visited = [False] * n
        heap = [(0, 0)]  # (cost, node)
        total = 0
        edges_used = 0
        while edges_used < n:
            cost, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            total += cost
            edges_used += 1
            for v in range(n):  # O(n) neighbors
                if not visited[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(heap, (d, v))  # O(log(n^2)) = O(log n)
        return total


class Solution2:
    """Kruskal's algorithm with Union-Find. O(n^2 * log(n)) time, O(n^2) space."""

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path halving
                x = parent[x]
            return x

        def union(a, b) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        # build all edges: O(n^2) edges
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
        edges.sort()  # O(n^2 * log(n^2)) = O(n^2 * log n)

        total = 0
        edges_used = 0
        for cost, u, v in edges:
            if union(u, v):
                total += cost
                edges_used += 1
                if edges_used == n - 1:
                    break
        return total
