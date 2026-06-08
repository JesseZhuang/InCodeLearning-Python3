class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """Monotonic stack greedy approach."""
        stack = []
        for digit in num:  # O(n)
            while k and stack and stack[-1] > digit:  # O(1) amortized, each digit pushed/popped at most once
                stack.pop()
                k -= 1
            stack.append(digit)
        # Remove remaining k digits from the end
        if k:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"
