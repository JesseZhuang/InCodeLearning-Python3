"""leet 1765, lint 974, leet 542, medium"""
from collections import deque


class Solution1:
    """
    542, 52 ms, 19.65 mb
    1765, 501 ms, 76.47 mb
    """

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        INF = m + n
        for r in range(m):
            for c in range(n):
                # mat[r][c] = 1 - mat[r][c]  # uncomment this line for 1765
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else INF
                    left = mat[r][c - 1] if c > 0 else INF
                    mat[r][c] = min(top, left) + 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else INF
                    right = mat[r][c + 1] if c < n - 1 else INF
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
        return mat


class Solution2:
    """
    542, 122 ms, 19.20 mb
    1765, 775 ms, 76.98 mb
    """

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]
        q = deque()
        for r in range(m):
            for c in range(n):
                mat[r][c] = 1 - mat[r][c]  # uncomment this line for 1765
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat
