"""leet 802, medium, tags: graph, dfs, bfs, topological sort."""

from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        """DFS 3-coloring. O(V+E) time, O(V) space."""
        n = len(graph)
        color = [0] * n  # 0: unvisited, 1: visiting, 2: safe

        def dfs(node: int) -> bool:
            """Returns True if node is safe."""
            if color[node] != 0:
                return color[node] == 2
            color[node] = 1  # O(1) mark visiting
            for nei in graph[node]:  # O(out-degree) per node, O(E) total
                if not dfs(nei):
                    return False
            color[node] = 2
            return True

        return [i for i in range(n) if dfs(i)]

    def eventualSafeNodesBFS(self, graph: list[list[int]]) -> list[int]:
        """Reverse graph + topological sort BFS. O(V+E) time, O(V+E) space."""
        n = len(graph)
        out_degree = [0] * n
        rev = [[] for _ in range(n)]  # O(V+E) space for reverse adjacency list
        for u in range(n):
            out_degree[u] = len(graph[u])  # O(V)
            for v in graph[u]:
                rev[v].append(u)  # O(E) total
        q = deque(u for u in range(n) if out_degree[u] == 0)
        safe = [False] * n
        while q:  # O(V+E) BFS on reverse graph
            node = q.popleft()
            safe[node] = True
            for prev in rev[node]:
                out_degree[prev] -= 1
                if out_degree[prev] == 0:
                    q.append(prev)
        return [i for i in range(n) if safe[i]]
