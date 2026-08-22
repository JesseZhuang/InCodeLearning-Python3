"""LeetCode 785, medium, tags: graph, dfs, bfs, union find."""
from collections import deque
from typing import List


class Solution:
    """BFS coloring. Try to 2-color the graph; if a neighbor has the same color, not bipartite.

    Complexity: Time O(V+E), Space O(V).
    """

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n  # 0: unvisited, 1 or -1: two colors
        for i in range(n):  # O(V) handle disconnected components
            if color[i] != 0:
                continue
            color[i] = 1
            queue = deque([i])
            while queue:  # O(V+E) BFS
                node = queue.popleft()
                for nei in graph[node]:  # O(degree) per node
                    if color[nei] == 0:
                        color[nei] = -color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False
        return True


class Solution2:
    """Union-Find. For each node, all its neighbors must be in the same group (opposite to the node).

    Complexity: Time O(V * alpha(V) + E), Space O(V).
    """

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:  # O(alpha(V)) amortized with path compression
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1

        for node in range(n):  # O(V)
            for nei in graph[node]:  # O(E) total across all nodes
                if find(node) == find(nei):  # node and neighbor in same set
                    return False
                union(graph[node][0], nei)  # all neighbors go into same group
        return True
