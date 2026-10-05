from collections import deque


class Solution:
    """1129. BFS over (node, last color): O(n + m) time and space."""

    def shortestAlternatingPaths(
        self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]
    ) -> list[int]:
        graph = [[[] for _ in range(n)] for _ in range(2)]
        for color, edges in enumerate((redEdges, blueEdges)):
            for source, target in edges:
                graph[color][source].append(target)

        shortest = [-1] * n
        shortest[0] = 0
        visited = [[False, False] for _ in range(n)]
        queue = deque([(0, -1, 0)])

        while queue:
            node, last_color, distance = queue.popleft()
            for color in range(2):
                if color == last_color:
                    continue
                for neighbor in graph[color][node]:
                    if visited[neighbor][color]:
                        continue
                    visited[neighbor][color] = True
                    if shortest[neighbor] == -1:
                        shortest[neighbor] = distance + 1
                    queue.append((neighbor, color, distance + 1))

        return shortest
