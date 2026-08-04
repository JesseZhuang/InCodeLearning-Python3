"""leet code 678, medium, tags: string, greedy, stack, dynamic programming."""


class Solution:
    """Greedy with min/max open count. O(n) time, O(1) space."""

    def checkValidString(self, s: str) -> bool:
        lo = 0  # min possible open '(' count
        hi = 0  # max possible open '(' count
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:  # '*' can be '(', ')' or empty
                lo -= 1  # treat as ')'
                hi += 1  # treat as '('
            if hi < 0:  # too many ')' even treating all '*' as '('
                return False
            lo = max(lo, 0)  # lo can't go negative (don't need extra ')')
        return lo == 0


class Solution2:
    """Two-pass greedy. O(n) time, O(1) space."""

    def checkValidString(self, s: str) -> bool:
        # left to right: ensure ')' never exceeds '(' + '*'
        balance = 0
        for c in s:
            if c == '(' or c == '*':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        # right to left: ensure '(' never exceeds ')' + '*'
        balance = 0
        for c in reversed(s):
            if c == ')' or c == '*':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return True
