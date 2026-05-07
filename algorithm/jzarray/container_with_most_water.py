class Solution:
    """LeetCode 11. Container With Most Water. Medium.
    Tags: array, two pointers, greedy.
    """

    # O(n) time, O(1) space. Two pointers with skip optimization.
    def maxArea(self, height: list[int]) -> int:
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res = max(res, (r - l) * h)
            while l < r and height[l] <= h:  # O(n) total moves across all iterations
                l += 1
            while l < r and height[r] <= h:
                r -= 1
        return res


class Solution2:
    """Two pointers, simpler version. O(n) time, O(1) space."""

    def maxArea(self, height: list[int]) -> int:
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
