class Solution:
    """1249. Minimum Remove to Make Valid Parentheses

    Stack approach: track indices of unmatched parentheses, rebuild string skipping them.
    """

    def min_remove_to_make_valid(self, s: str) -> str:
        stack = []  # indices of unmatched '('
        to_remove = set()
        for i, c in enumerate(s):  # O(n)
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        to_remove.update(stack)  # remaining unmatched '('
        return ''.join(c for i, c in enumerate(s) if i not in to_remove)  # O(n)


class Solution2:
    """Two-pass approach: left-to-right removes excess ')', right-to-left removes excess '('."""

    def min_remove_to_make_valid(self, s: str) -> str:
        # Pass 1: remove excess ')' — O(n)
        result = []
        open_count = 0
        for c in s:
            if c == '(':
                open_count += 1
                result.append(c)
            elif c == ')':
                if open_count > 0:
                    open_count -= 1
                    result.append(c)
            else:
                result.append(c)
        # Pass 2: remove excess '(' from the right — O(n)
        final = []
        close_needed = 0
        for c in reversed(result):
            if c == '(':
                if close_needed > 0:
                    close_needed -= 1
                else:
                    continue
            elif c == ')':
                close_needed += 1
            final.append(c)
        return ''.join(reversed(final))
