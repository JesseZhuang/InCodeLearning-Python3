"""leet code 1249, medium"""

from collections import deque


class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:
        """90ms, 18.30MB"""
        l, r = 0, 0
        for c in s:
            if c == ')': r += 1
        res = []
        for c in s:
            if c == '(':
                if l == r: continue
                l += 1
            elif c == ')':
                r -= 1
                if l == 0: continue
                l -= 1
            res.append(c)
        return ''.join(res)


class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        """79ms, 18.2MB"""
        sa = list(s)
        stack = deque()
        for i, c in enumerate(sa):
            if c == '(':
                stack.append(i)  # note: not push()
            elif c == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    sa[i] = ''
        while len(stack) > 0: sa[stack.pop()] = ''
        return ''.join(sa)
