"""leet code 36, medium"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                s = board[r][c]
                if s == ".": continue;
                if (r, s) in seen or (s, c) in seen or (r // 3, c // 3, s) in seen:
                    return False
                else:
                    seen.add((r, s))
                    seen.add((s, c))
                    seen.add((r // 3, c // 3, s))
        return True
