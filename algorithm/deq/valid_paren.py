"""leet code 20, easy"""

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        for c in s:
            match c:
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
