"""leet 42, hard, tags: array, two pointers, dynamic programming, stack, monotonic stack."""


class Solution:
    def trap(self, height: list[int]) -> int:
        """Two pointers approach.

        Time O(n), Space O(1).
        """
        l, r = 0, len(height) - 1  # O(1)
        l_max, r_max, res = 0, 0, 0
        while l < r:  # O(n), each element visited at most once
            if height[l] <= height[r]:
                l_max = max(l_max, height[l])
                res += l_max - height[l]  # water trapped at index l
                l += 1
            else:
                r_max = max(r_max, height[r])
                res += r_max - height[r]  # water trapped at index r
                r -= 1
        return res


class Solution2:
    def trap(self, height: list[int]) -> int:
        """Monotonic stack approach.

        Time O(n), Space O(n).
        """
        stack = []  # O(n) space, stores indices
        res = 0
        for i, h in enumerate(height):  # O(n), each index pushed and popped at most once
            while stack and height[stack[-1]] < h:
                mid = stack.pop()
                if not stack:
                    break
                width = i - stack[-1] - 1
                bounded_height = min(h, height[stack[-1]]) - height[mid]
                res += width * bounded_height
            stack.append(i)
        return res
