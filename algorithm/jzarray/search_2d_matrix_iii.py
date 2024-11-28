"""lint 38, medium"""


class Solution:
    """
    m+n, mn
    todo, editorial
    """

    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix[0] == []:
            return 0

        row, column = len(matrix), len(matrix[0])
        i, j = row - 1, 0
        count = 0
        while i >= 0 and j < column:
            if matrix[i][j] == target:
                count += 1
                i -= 1
                j += 1
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return count
