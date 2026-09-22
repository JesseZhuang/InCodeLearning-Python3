"""leet 542, medium, tags: array, dynamic programming, bfs, matrix."""

from collections import deque


class Solution:
    """DP two-pass. O(m*n) time, O(1) space (in-place)."""

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        INF = m + n
        for r in range(m):  # O(m*n) top-left to bottom-right
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else INF
                    left = mat[r][c - 1] if c > 0 else INF
                    mat[r][c] = min(top, left) + 1
        for r in range(m - 1, -1, -1):  # O(m*n) bottom-right to top-left
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else INF
                    right = mat[r][c + 1] if c < n - 1 else INF
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
        return mat


class Solution2:
    """Multi-source BFS. O(m*n) time, O(m*n) space."""

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        q = deque()
        for r in range(m):  # O(m*n)
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
        while q:  # O(m*n) total
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
        return mat
