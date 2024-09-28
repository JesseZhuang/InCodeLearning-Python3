"""leet code 844, easy"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """32ms, 16.5mb"""
        i, j = len(s) - 1, len(t) - 1

        def move(i: int, s: str) -> int:
            back = 0
            while i >= 0:
                if s[i] == "#":
                    back += 1
                    i -= 1
                elif back:
                    back -= 1
                    i -= 1
                else:
                    break
            return i

        while True:
            i = move(i, s)
            j = move(j, t)
            if not (i >= 0 and j >= 0 and s[i] == t[j]):
                return i == j == -1
            i -= 1
            j -= 1
