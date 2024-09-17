"""leet code 79, medium, lint code 123"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """4274ms, 16.6mb"""
        m, n = len(board), len(board[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r: int, c: int, i: int) -> bool:
            if r < 0 or r > m - 1 or c < 0 or c > n - 1: return False
            tmp = board[r][c]
            if word[i] != tmp: return False
            if i == len(word) - 1: return True
            board[r][c] = "#"
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if dfs(nr, nc, i + 1): return True
            board[r][c] = tmp
            return False

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0): return True
        return False
