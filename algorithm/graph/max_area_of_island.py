"""leet code 695, medium, tags: array, depth-first search, breadth-first search, union find, matrix."""
from collections import deque
from typing import List


class Solution:
    """DFS. O(m*n) time, O(m*n) space (recursion stack worst case)."""

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(r, c) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = 0  # mark visited
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)  # O(m*n) total

        for i in range(m):  # O(m)
            for j in range(n):  # O(n)
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res


class Solution2:
    """BFS. O(m*n) time, O(min(m,n)) space (queue size)."""

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):  # O(m)
            for j in range(n):  # O(n)
                if grid[i][j] == 1:
                    area = 0
                    grid[i][j] = 0
                    q = deque([(i, j)])
                    while q:  # O(m*n) total across all calls
                        r, c = q.popleft()
                        area += 1
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                q.append((nr, nc))
                    res = max(res, area)
        return res
