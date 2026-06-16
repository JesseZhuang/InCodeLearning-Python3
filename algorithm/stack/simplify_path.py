"""LeetCode 71, medium, tags: string, stack."""


class Solution:
    """Stack approach. Split by '/', push valid components, pop for '..'."""

    def simplifyPath(self, path: str) -> str:
        stack = []  # O(n) space
        for part in path.split('/'):  # O(n) time
            if part == '..':
                if stack:
                    stack.pop()
            elif part and part != '.':
                stack.append(part)
        return '/' + '/'.join(stack)
