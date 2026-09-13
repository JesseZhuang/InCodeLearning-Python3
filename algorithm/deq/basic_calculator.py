"""leet code 224, hard, tags: math, string, stack, recursion."""
from collections import deque


class Solution:
    """Stack. O(n) time, O(n) space."""

    def calculate(self, s: str) -> int:
        vals = deque()
        res, sign, i = 0, 1, 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                n = int(c)
                while i + 1 < len(s) and s[i + 1].isdigit():  # O(digits) per number
                    n = n * 10 + int(s[i + 1])
                    i += 1
                res += n * sign
            elif c == "-":
                sign = -1
            elif c == "+":
                sign = 1
            elif c == "(":  # O(1) push
                vals.append(res)
                vals.append(sign)
                res = 0
                sign = 1
            elif c == ")":  # O(1) pop
                res = res * vals.pop() + vals.pop()
            i += 1
        return res


class Solution2:
    """Recursive descent parser. O(n) time, O(depth) space for recursion stack."""

    def calculate(self, s: str) -> int:
        self.i = 0
        self.s = s
        return self._expr()

    def _expr(self) -> int:
        res = self._num()
        while self.i < len(self.s):
            self._skip_spaces()
            if self.i >= len(self.s) or self.s[self.i] == ')':
                break
            op = self.s[self.i]
            self.i += 1
            right = self._num()
            if op == '+':
                res += right
            else:  # '-'
                res -= right
        return res

    def _num(self) -> int:
        self._skip_spaces()
        if self.s[self.i] == '(':  # recurse into sub-expression, O(depth)
            self.i += 1
            val = self._expr()
            self.i += 1  # skip ')'
            return val
        if self.s[self.i] == '-':  # unary minus
            self.i += 1
            return -self._num()
        n = 0
        while self.i < len(self.s) and self.s[self.i].isdigit():  # O(digits) per number
            n = n * 10 + int(self.s[self.i])
            self.i += 1
        self._skip_spaces()
        return n

    def _skip_spaces(self):
        while self.i < len(self.s) and self.s[self.i] == ' ':
            self.i += 1
