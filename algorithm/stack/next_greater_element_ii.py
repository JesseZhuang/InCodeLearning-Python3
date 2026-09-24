class Solution:
    """Monotonic decreasing stack with double traversal for circular array.

    Iterate indices 0..2n-1, using i%n to wrap around.
    Pop indices where current element is greater, recording the answer.
    """

    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n  # O(n) space
        stack = []  # monotonic decreasing stack of indices, O(n) space
        for i in range(2 * n):  # O(n), each index pushed/popped at most once across both passes
            while stack and nums[stack[-1]] < nums[i % n]:  # O(n) total pops
                res[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        return res  # Time O(n), Space O(n)


class Solution2:
    """Brute force: for each element, scan forward circularly."""

    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n  # O(n) space
        for i in range(n):  # O(n)
            for j in range(1, n):  # O(n)
                if nums[(i + j) % n] > nums[i]:
                    res[i] = nums[(i + j) % n]
                    break
        return res  # Time O(n^2), Space O(n)
