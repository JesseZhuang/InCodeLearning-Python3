from collections import deque


class Solution:
    """LeetCode 130, medium, tags: array, dfs, bfs, union find, matrix."""

    # BFS from boundary. O(mn) time and space.
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':
                    queue.append((i, j))
                    board[i][j] = '*'
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    board[nr][nc] = '*'
                    queue.append((nr, nc))
        for i in range(m):  # O(mn)
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'


class Solution2:
    """Union Find approach. O(mn * alpha(mn)) ~ O(mn) time, O(mn) space."""

    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        parent = list(range(m * n + 1))
        rank = [0] * (m * n + 1)
        dummy = m * n  # virtual node for boundary-connected cells

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        for i in range(m):
            for j in range(n):
                if board[i][j] != 'O':
                    continue
                idx = i * n + j
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    union(idx, dummy)
                if i > 0 and board[i - 1][j] == 'O':
                    union(idx, (i - 1) * n + j)
                if j > 0 and board[i][j - 1] == 'O':
                    union(idx, i * n + j - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and find(i * n + j) != find(dummy):
                    board[i][j] = 'X'
