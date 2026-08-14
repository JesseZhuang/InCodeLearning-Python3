class Solution:
    """Monotonic stack scanning from right to left.

    Maintain a decreasing stack and track the largest popped value as the '2' candidate.
    If any nums[i] < '2' candidate, we found a valid 132 pattern.
    """

    def find132pattern(self, nums: list[int]) -> bool:
        stack = []  # monotonic decreasing stack, O(n) space
        second = float('-inf')  # the '2' in 132 (largest value popped)
        for i in range(len(nums) - 1, -1, -1):  # O(n) scan right to left
            if nums[i] < second:  # nums[i] is '1', second is '2', stack top was '3'
                return True
            while stack and stack[-1] < nums[i]:  # O(n) total pops
                second = stack.pop()
            stack.append(nums[i])
        return False  # Time O(n), Space O(n)


class Solution2:
    """Prefix min + monotonic stack scanning from left to right.

    Use prefix_min[i] as the '1' candidate, then use a decreasing stack to find
    a valid '2' (stack element between prefix_min[i] and nums[i]).
    """

    def find132pattern(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        prefix_min = [0] * n  # O(n) space
        prefix_min[0] = nums[0]
        for i in range(1, n):  # O(n)
            prefix_min[i] = min(prefix_min[i - 1], nums[i])
        stack = []  # monotonic decreasing stack, O(n) space
        for j in range(n - 1, -1, -1):  # O(n) scan right to left
            if nums[j] > prefix_min[j]:
                while stack and stack[-1] <= prefix_min[j]:  # O(n) total pops
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True  # prefix_min[j] < stack[-1] < nums[j]
                stack.append(nums[j])
        return False  # Time O(n), Space O(n)
