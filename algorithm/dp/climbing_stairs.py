class Solution:
    """LeetCode 70 Climbing Stairs."""

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        previous, current = 1, 2
        # Each iteration computes one step: O(n) time and O(1) extra space.
        for _ in range(3, n + 1):
            previous, current = current, previous + current
        return current
