"""leet 1727, medium"""


class Solution1:
    """Sort heights per row."""

    # 129ms, 33.62mb
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        res = 0
        for i in range(m):
            row = matrix[i]
            for j in range(n):
                if row[j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            sorted_heights = sorted(heights, reverse=True)
            for k, h in enumerate(sorted_heights):
                if h == 0:
                    break
                res = max(h * (k + 1), res)
        return res


class Solution2:
    """Maintain sorted heights incrementally without per-row sort."""

    # 159ms, 33.84mb
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        prev_heights: list[tuple[int, int]] = []
        res = 0

        for row in range(m):
            heights: list[tuple[int, int]] = []
            seen = [False] * n

            for height, col in prev_heights:
                if matrix[row][col] == 1:
                    heights.append((height + 1, col))
                    seen[col] = True

            for col in range(n):
                if not seen[col] and matrix[row][col] == 1:
                    heights.append((1, col))

            for i, (h, _) in enumerate(heights):
                res = max(res, h * (i + 1))

            prev_heights = heights

        return res
