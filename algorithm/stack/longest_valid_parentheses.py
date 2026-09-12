class Solution:
    """32. Longest Valid Parentheses

    Stack approach: push indices; -1 as base for length calculation.
    """

    def longest_valid_parentheses(self, s: str) -> int:
        stack = [-1]  # base index for length calculation, O(n) space
        max_len = 0
        for i, c in enumerate(s):  # O(n)
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # new base
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


class Solution2:
    """Two-pass approach: O(1) space. Count open/close left-to-right and right-to-left."""

    def longest_valid_parentheses(self, s: str) -> int:
        max_len = 0
        # Left to right — O(n)
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0
        # Right to left — O(n), catches cases like "(()"
        left = right = 0
        for c in reversed(s):
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0
        return max_len
