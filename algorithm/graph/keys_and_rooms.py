"""LeetCode 841, medium, tags: graph, dfs, bfs."""

from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """DFS iterative. O(N+E) time, O(N) space where N=rooms, E=total keys."""
        visited = set()
        stack = [0]
        while stack:
            room = stack.pop()
            if room in visited:
                continue
            visited.add(room)
            for key in rooms[room]:  # O(E) total across all iterations
                if key not in visited:
                    stack.append(key)
        return len(visited) == len(rooms)

    def canVisitAllRoomsBFS(self, rooms: List[List[int]]) -> bool:
        """BFS. O(N+E) time, O(N) space."""
        visited = set([0])
        queue = deque([0])
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        return len(visited) == len(rooms)
