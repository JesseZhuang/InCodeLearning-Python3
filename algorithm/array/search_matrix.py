'''lc 240 medium'''

from typing import List


class Solution(object):
    def searchMatrix1(self, matrix, target):
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

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        print('target', target)
        return self.helper(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1, target)
    
    # top left, bottom right bound
    def helper(self, matrix, r1, c1, r2, c2, target):
        # print(r1, c1, r2, c2)
        if r2 < r1 or c2 < c1 or r1 >= len(matrix) or c1 >= len(matrix[0]):
            return False
        r_mid = (r1+r2)//2
        c_mid = (c1+c2)//2
        v = matrix[r_mid][c_mid]
        # print('v', v, 't', target)
        # print(v == target)
        if v < target:  # 
            return self.helper(matrix, r1, c_mid+1, r_mid, c2, target) \
                or self.helper(matrix, r_mid+1, c1, r2, c_mid, target)  \
                or self.helper(matrix, r_mid+1, c_mid+1, r2, c2, target)
        elif v > target:
            return self.helper(matrix, r1, c1, r_mid, c_mid-1, target) \
                or self.helper(matrix, r1, c_mid, r_mid-1, c2, target) \
                or self.helper(matrix, r_mid+1, c1, r2, c_mid-1, target)
        else:
            return True
