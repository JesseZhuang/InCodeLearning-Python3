class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """Monotonic stack + greedy. O(n) time, O(1) space (26 letters)."""
        last_index = {c: i for i, c in enumerate(s)}  # O(n)
        stack = []
        in_stack = set()
        for i, c in enumerate(s):  # O(n)
            if c in in_stack:
                continue
            while stack and c < stack[-1] and last_index[stack[-1]] > i:  # O(1) amortized
                in_stack.discard(stack.pop())
            stack.append(c)
            in_stack.add(c)
        return "".join(stack)
