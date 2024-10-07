"""leet code 2696, easy"""
from collections import deque


class Solution:
    def minLength(self, s: str) -> int:
        st = deque()
        for c in s:
            if st and ((c == 'B' and st[-1] == 'A') or (c == 'D' and st[-1] == 'C')):
                st.pop()
            else:
                st.append(c)
        return len(st)
