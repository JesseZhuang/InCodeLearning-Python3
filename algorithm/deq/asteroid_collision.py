"""LeetCode 735, medium, tags: array, stack, simulation."""


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack: list[int] = []
        for a in asteroids:  # O(n)
            alive = True
            while alive and a < 0 and stack and stack[-1] > 0:  # each element pushed/popped at most once, O(n) total
                if stack[-1] < -a:
                    stack.pop()
                elif stack[-1] == -a:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(a)
        return stack  # Time O(n), Space O(n)
