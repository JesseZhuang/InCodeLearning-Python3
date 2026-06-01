"""leet 1091, medium"""

from collections import deque


class Solution:
    """BFS, O(n^2) time, O(n^2) space."""

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        q = deque([(0, 0, 1)])
        grid[0][0] = 1  # mark visited
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while q:
            r, c, dist = q.popleft()
            if r == n - 1 and c == n - 1:
                return dist
            for dr, dc in dirs:  # O(8) per cell
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc, dist + 1))
        return -1


class Solution2:
    """A* with Chebyshev distance heuristic, O(n^2 log n) time, O(n^2) space."""

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        import heapq
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        # (estimated_total, dist, row, col)
        heap = [(n - 1, 1, 0, 0)]
        grid[0][0] = 1
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while heap:
            _, dist, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return dist
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    h = max(n - 1 - nr, n - 1 - nc)  # Chebyshev distance
                    heapq.heappush(heap, (dist + 1 + h, dist + 1, nr, nc))
        return -1
