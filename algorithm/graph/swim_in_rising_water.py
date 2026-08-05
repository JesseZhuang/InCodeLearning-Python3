import heapq
from collections import deque


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """Min-Heap (Dijkstra-like). Time O(n^2 log n), Space O(n^2)."""
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        # (max elevation along path, row, col)
        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        return -1


class Solution2:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """Binary Search + BFS. Time O(n^2 log n), Space O(n^2)."""
        n = len(grid)

        def can_reach(t: int) -> bool:
            if grid[0][0] > t:
                return False
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            queue = deque([(0, 0)])
            while queue:
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] <= t:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            return False

        lo, hi = max(grid[0][0], grid[n - 1][n - 1]), n * n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if can_reach(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
