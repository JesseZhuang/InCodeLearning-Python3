'''lc 240 medium'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r, c = 0, len(matrix[0])-1
        while r < len(matrix) and c >= 0:
            v = matrix[r][c]
            if v == target: return True
            elif v < target: r += 1
            else: c -= 1
        return False
