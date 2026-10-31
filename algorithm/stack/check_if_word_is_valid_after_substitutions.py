class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for character in s:  # O(n) total: every character is pushed and popped at most once.
            stack.append(character)
            if stack[-3:] == ["a", "b", "c"]:
                del stack[-3:]
        return not stack  # O(n) auxiliary space in the worst case.
