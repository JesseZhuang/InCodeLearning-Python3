"""leet code 1106, hard"""
from collections import deque


class Solution2:
    """@lee215, fun"""

    def parseBoolExpr(self, S, t=True, f=False) -> bool:
        return eval(S.replace('!', 'not |').replace('&(', 'all([').replace('|(', 'any([').replace(')', '])'))


class Solution1:
    def parseBoolExpr(self, expression):
        e, st = expression, deque()
        for c in e:
            if c in ',(': continue
            if c != ')':
                st.append(c)
            else:
                has_true, has_false = False, False
                while st[-1] not in '|&!':
                    ch = st.pop()
                    if ch == 't': has_true = True
                    if ch == 'f': has_false = True
                op = st.pop()
                match op:
                    case '!':
                        st.append('t' if has_false else 'f')
                    case '&':
                        st.append('f' if has_false else 't')
                    case _:
                        st.append('t' if has_true else 'f')
        return st[-1] == 't'
