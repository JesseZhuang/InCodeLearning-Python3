"""leet code 864, hard"""
from collections import deque
from typing import List


class Solution:
    """186ms, 21.3mb"""

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        def k_i(c):
            return ord(c) - ord("a")

        def l_i(c):
            return ord(c) - ord("A")

        m, n = len(grid), len(grid[0])
        x, y, kc = -1, -1, 0  # starting point, key count
        for r in range(m):
            for c in range(n):
                ch = grid[r][c]
                if ch == "@":
                    x, y = r, c
                elif "a" <= ch <= "f":
                    kc += 1
        q = deque()
        visited, keys = set(), 0
        res = 0
        q.append((x, y, keys))
        visited.add((x, y, keys))
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while q:
            size = len(q)
            for i in range(size):
                cr, cc, ck = q.popleft()
                if ck == (1 << kc) - 1: return res
                for d in dirs:
                    nr, nc, nk = cr + d[0], cc + d[1], ck
                    if nr < 0 or nr > m - 1 or nc < 0 or nc > n - 1: continue
                    ch = grid[nr][nc]
                    if ch == "#": continue
                    if "A" <= ch <= "F" and (nk & (1 << l_i(ch))) == 0: continue
                    if (nr, nc, nk) in visited: continue
                    if "a" <= ch <= "f": nk |= 1 << k_i(ch)
                    q.append((nr, nc, nk))
                    visited.add((nr, nc, nk))
            res += 1
        return -1
