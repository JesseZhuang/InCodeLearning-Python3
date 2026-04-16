"""LeetCode 155, medium, tags: stack, design."""


class MinStack:
    """Two stacks approach. Each operation is O(1) time. O(n) space."""

    def __init__(self):
        self.stack = []
        self.min_stack = []  # tracks current min at each level

    def push(self, val: int) -> None:
        self.stack.append(val)  # O(1)
        # push the new min onto min_stack
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))  # O(1)

    def pop(self) -> None:
        self.stack.pop()  # O(1)
        self.min_stack.pop()  # O(1)

    def top(self) -> int:
        return self.stack[-1]  # O(1)

    def getMin(self) -> int:
        return self.min_stack[-1]  # O(1)


class MinStackSingleStack:
    """Single stack storing (val, current_min) tuples. Each operation is O(1) time. O(n) space."""

    def __init__(self):
        self.stack = []  # stores (val, current_min) tuples

    def push(self, val: int) -> None:
        cur_min = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, cur_min))  # O(1)

    def pop(self) -> None:
        self.stack.pop()  # O(1)

    def top(self) -> int:
        return self.stack[-1][0]  # O(1)

    def getMin(self) -> int:
        return self.stack[-1][1]  # O(1)
