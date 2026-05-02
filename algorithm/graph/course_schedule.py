"""leet code 207, medium, tags: depth-first search, breadth-first search, graph, topological sort."""
from collections import defaultdict, deque
from typing import List


class Solution:
    """Iterative DFS cycle detection. O(V+E) time, O(V+E) space."""

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in prerequisites:  # b is prerequisite of a
            adj[b].append(a)
        WHITE, GRAY, BLACK = 0, 1, 2  # unvisited, on stack, done
        color = [WHITE] * numCourses

        for start in range(numCourses):  # O(V) outer loop
            if color[start] != WHITE:
                continue
            stack = [(start, 0)]
            color[start] = GRAY
            while stack:  # O(V+E) total across all starts
                u, idx = stack.pop()
                if idx < len(adj[u]):
                    stack.append((u, idx + 1))
                    v = adj[u][idx]
                    if color[v] == GRAY:
                        return False
                    if color[v] == WHITE:
                        color[v] = GRAY
                        stack.append((v, 0))
                else:
                    color[u] = BLACK
        return True


class Solution2:
    """BFS topological sort (Kahn's algorithm). O(V+E) time, O(V+E) space."""

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:  # O(E) build adjacency list
            adj[b].append(a)
            in_degree[a] += 1
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        count = 0
        while queue:  # O(V+E) process all nodes and edges
            u = queue.popleft()
            count += 1
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        return count == numCourses
