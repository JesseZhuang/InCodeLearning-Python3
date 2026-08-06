class Solution:
    """Monotonic decreasing stack of indices.

    For each temperature, pop indices where current temp is warmer,
    computing the wait as the index difference.
    """

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n  # O(n) space
        stack = []  # monotonic decreasing stack of indices, O(n) space
        for i in range(n):  # O(n)
            while stack and temperatures[stack[-1]] < temperatures[i]:  # O(n) total pops
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res  # Time O(n), Space O(n)
