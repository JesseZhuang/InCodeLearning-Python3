"""leet code 1293, hard"""
from collections import deque
from typing import List


class Solution:
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (r, c), res = map(len, (grid, grid[0])), 0
        start = (0, 0, 0)
        mark, q = set(), deque()
        mark.add(start)  # marked=[[[False]*(k+1) for _ in range(n)] for _ in range(m)] if want to use 3d array
        q.append(start)
        while q:
            size = len(q)
            for i in range(size):
                (cr, cc, ck) = q.popleft()
                if cr == r - 1 and cc == c - 1: return res
                for d in Solution.dirs:
                    nr, nc, nk = cr + d[0], cc + d[1], ck
                    if nr < 0 or nr > r - 1 or nc < 0 or nc > c - 1: continue
                    if grid[nr][nc] == 1: nk += 1
                    state = (nr, nc, nk)
                    if nk > k or state in mark: continue
                    mark.add(state)
                    q.append(state)
            res += 1
        return -1
