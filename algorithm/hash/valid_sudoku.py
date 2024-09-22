"""leet code 36, medium"""

from typing import List


class Solution:
    """96ms, 16.61mb"""

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                s = board[r][c]
                if s == ".": continue
                s1, s2, s3 = (r, s), (s, c), (r // 3, c // 3, s)
                if any(state in seen for state in [s1, s2, s3]):
                    return False
                else:
                    seen.update([s1, s2, s3])
        return True
