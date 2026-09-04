"""LeetCode 289, medium, tags: array, matrix, simulation."""


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """In-place with state encoding. O(mn) time, O(1) space.
        Encode [next_state, current_state] in two bits.
        """
        m, n = len(board), len(board[0])
        for r in range(m):  # O(m)
            for c in range(n):  # O(n)
                count = 0
                for i in range(max(r - 1, 0), min(r + 2, m)):  # O(1), at most 3
                    for j in range(max(c - 1, 0), min(c + 2, n)):  # O(1), at most 3
                        count += board[i][j] & 1
                # count includes board[r][c] itself
                if count == 3 or count - board[r][c] == 3:
                    board[r][c] |= 2  # set next state to alive
        for r in range(m):  # O(m)
            for c in range(n):  # O(n)
                board[r][c] >>= 1


class Solution2:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """Copy board. O(mn) time, O(mn) space."""
        m, n = len(board), len(board[0])
        copy = [row[:] for row in board]  # O(mn) space
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for r in range(m):  # O(m)
            for c in range(n):  # O(n)
                count = sum(
                    copy[r + dr][c + dc]
                    for dr, dc in dirs  # O(1), 8 directions
                    if 0 <= r + dr < m and 0 <= c + dc < n
                )
                if board[r][c] == 1 and (count < 2 or count > 3):
                    board[r][c] = 0
                elif board[r][c] == 0 and count == 3:
                    board[r][c] = 1
