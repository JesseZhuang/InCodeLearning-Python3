"""leet code 79, medium, lint code 123"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(0, m):
            for j in range(0, n):
                if self.dfs(board, i, j, 0, word): return True
        return False

    def dfs(self, board, r, c, index, word):
        m, n = len(board), len(board[0])
        if index == len(word): return True
        if r >= m or c >= n or r < 0 or c < 0 or board[r][c] == '8' or board[r][c] != word[index]:
            return False
        temp = board[r][c]
        board[r][c] = '8'
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for dr in dirs:
            if self.dfs(board, r + dr[0], c + dr[1], index + 1, word): return True
        board[r][c] = temp
        return False
