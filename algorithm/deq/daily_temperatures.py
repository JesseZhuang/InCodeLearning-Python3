"""LeetCode 739, medium, tags: array, stack, monotonic stack."""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # monotonic decreasing stack of indices
        for i, t in enumerate(temperatures):  # O(n)
            while stack and temperatures[stack[-1]] < t:  # each index pushed/popped at most once, O(n) total
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res  # Time O(n), Space O(n)
