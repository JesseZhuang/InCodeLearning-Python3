"""leet 994, lint 3726, medium"""

from collections import deque


class Solution:
    """6 ms, 17.32 mb"""

    def orangesRotting(self, grid: list[list[int]]) -> int:
        (m, n), fresh, q, res = map(len, (grid, grid[0])), 0, deque(), 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        while q and fresh > 0:
            res += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx == m or ny < 0 or ny == n: continue
                    if grid[nx][ny] == 0 or grid[nx][ny] == 2: continue
                    fresh -= 1
                    grid[nx][ny] = 2  # serve as visited
                    q.append((nx, ny))
        return res if fresh == 0 else -1
