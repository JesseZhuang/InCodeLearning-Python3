"""LeetCode 84, hard, tags: array, stack, monotonic stack."""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack = []  # monotonic increasing stack of indices
        max_area = 0
        for i in range(n + 1):  # O(n)
            h = 0 if i == n else heights[i]
            while stack and h < heights[stack[-1]]:  # each index pushed/popped once, O(n) total
                cur_height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, cur_height * width)
            stack.append(i)
        return max_area  # Time O(n), Space O(n)


class Solution2:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        left_wall = [-1] * n
        right_wall = [n] * n
        for i in range(1, n):  # O(n) amortized
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = left_wall[p]
            left_wall[i] = p
        for i in range(n - 2, -1, -1):  # O(n) amortized
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = right_wall[p]
            right_wall[i] = p
        max_area = 0
        for i in range(n):  # O(n)
            max_area = max(max_area, heights[i] * (right_wall[i] - left_wall[i] - 1))
        return max_area  # Time O(n), Space O(n)
