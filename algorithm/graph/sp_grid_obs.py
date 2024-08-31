"""leet code 1293, hard"""
from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        visited = set()
        visited.add((0, 0, 0))
        q = deque()
        q.append((0, 0, 0))
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        res = 0
        while len(q) != 0:
            size = len(q)
            for i in range(size):
                (cr, cc, ck) = q.popleft()
                if cr == r - 1 and cc == c - 1: return res
                for d in dirs:
                    nr, nc, nk = cr + d[0], cc + d[1], ck
                    if nr < 0 or nr > r - 1 or nc < 0 or nc > c - 1: continue
                    if grid[nr][nc] == 1: nk += 1
                    if nk > k or (nr, nc, nk) in visited: continue
                    visited.add((nr, nc, nk))
                    q.append((nr, nc, nk))
            res += 1
        return -1
