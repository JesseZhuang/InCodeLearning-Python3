"""leet 1162, medium, tags: array, bfs, dynamic programming, matrix."""

from collections import deque


class Solution:
    """Multi-source BFS. O(n^2) time, O(n^2) space."""

    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        q = deque()
        for r in range(n):  # O(n^2) enqueue all land cells
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
        if len(q) == 0 or len(q) == n * n:
            return -1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = -1
        while q:  # O(n^2) each cell dequeued once
            dist += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:  # O(4) per cell
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))
        return dist


class Solution2:
    """DP two passes. O(n^2) time, O(1) space (in-place)."""

    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        INF = 2 * n
        has_land = has_water = False
        # top-left to bottom-right
        for r in range(n):  # O(n)
            for c in range(n):  # O(n)
                if grid[r][c] == 1:
                    has_land = True
                    grid[r][c] = 0
                else:
                    has_water = True
                    top = grid[r - 1][c] if r > 0 else INF
                    left = grid[r][c - 1] if c > 0 else INF
                    grid[r][c] = min(top, left) + 1
        if not has_land or not has_water:
            return -1
        # bottom-right to top-left
        res = 0
        for r in range(n - 1, -1, -1):  # O(n)
            for c in range(n - 1, -1, -1):  # O(n)
                if grid[r][c] > 0:
                    bottom = grid[r + 1][c] if r < n - 1 else INF
                    right = grid[r][c + 1] if c < n - 1 else INF
                    grid[r][c] = min(grid[r][c], bottom + 1, right + 1)
                    res = max(res, grid[r][c])
        return res
