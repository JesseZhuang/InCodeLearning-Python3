"""LeetCode 1306, medium, tags: array, graph, bfs, dfs."""

from collections import deque


class Solution:
    """BFS. O(n) time and O(n) space."""

    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        visited = {start}
        queue = deque([start])
        while queue:  # Each index is queued once: O(n) total work.
            index = queue.popleft()
            if arr[index] == 0:
                return True
            for neighbor in (index + arr[index], index - arr[index]):
                if 0 <= neighbor < n and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False


class Solution2:
    """Iterative DFS. O(n) time and O(n) space."""

    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        visited = {start}
        stack = [start]
        while stack:  # Each index is pushed once: O(n) total work.
            index = stack.pop()
            if arr[index] == 0:
                return True
            for neighbor in (index + arr[index], index - arr[index]):
                if 0 <= neighbor < n and neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return False
