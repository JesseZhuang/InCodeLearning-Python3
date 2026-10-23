class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for character in s:  # O(n) total: each character is pushed and popped at most once.
            if stack and stack[-1] == character:
                stack.pop()
            else:
                stack.append(character)
        return "".join(stack)  # O(n) time and O(n) auxiliary stack space.
