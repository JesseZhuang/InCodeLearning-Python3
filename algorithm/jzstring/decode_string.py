"""leet 394, medium, tags: string, stack, recursion."""


class Solution:
    """Stack-based approach. Time O(n * max_k), Space O(n)."""

    def decodeString(self, s: str) -> str:
        stack = []  # stack of (previous_string, repeat_count)
        cur = ""
        k = 0
        for c in s:  # O(n)
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                stack.append((cur, k))
                cur, k = "", 0
            elif c == ']':
                prev, cnt = stack.pop()
                cur = prev + cur * cnt  # O(max_k) per expansion
            else:
                cur += c
        return cur


class Solution2:
    """Recursive descent approach. Time O(n * max_k), Space O(n)."""

    def decodeString(self, s: str) -> str:
        self.i = 0
        return self._decode(s)

    def _decode(self, s: str) -> str:
        res = ""
        while self.i < len(s) and s[self.i] != ']':
            if s[self.i].isdigit():
                k = 0
                while self.i < len(s) and s[self.i].isdigit():  # parse number
                    k = k * 10 + int(s[self.i])
                    self.i += 1
                self.i += 1  # skip '['
                decoded = self._decode(s)  # recurse for nested content
                self.i += 1  # skip ']'
                res += decoded * k  # O(max_k)
            else:
                res += s[self.i]
                self.i += 1
        return res
