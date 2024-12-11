"""leet code 20, easy"""

from collections import deque


class Solution:
    """0 ms, 17.42 mb"""

    def isValid(self, s: str) -> bool:
        st = deque()
        for c in s:
            match c:  # match case since 3.10
                case '(':
                    st.append(')')
                case '[':
                    st.append(']')
                case '{':
                    st.append('}')
                case _:
                    if not st or st.pop() != c:
                        return False
        return len(st) == 0
