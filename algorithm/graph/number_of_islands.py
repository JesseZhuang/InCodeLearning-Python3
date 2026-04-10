"""leet code 200, medium, tags: array, depth-first search, breadth-first search, union find, matrix."""
from collections import deque
from typing import List


class Solution:
    """DFS. O(m*n) time, O(m*n) space (recursion stack worst case)."""

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return
            grid[r][c] = '0'  # mark visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(m):  # O(m)
            for j in range(n):  # O(n)
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)  # O(m*n) total across all calls
        return res


class Solution2:
    """BFS. O(m*n) time, O(min(m,n)) space (queue size)."""

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):  # O(m)
            for j in range(n):  # O(n)
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    q = deque([(i, j)])
                    while q:  # O(m*n) total across all calls
                        r, c = q.popleft()
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                q.append((nr, nc))
        return res
