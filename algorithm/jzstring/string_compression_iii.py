"""leet code 3163, medium"""
from itertools import groupby


class Solution:
    def compressedString(self, word: str) -> str:
        i, res = 0, list()
        while i < len(word):
            streak, c = 0, word[i]
            while i < len(word) and streak < 9 and word[i] == c:
                streak += 1
                i += 1
            res.append(str(streak))
            res.append(c)
        return ''.join(res)


class Solution2:
    def compressedString(self, word: str) -> str:
        # groupby('aaabba') -> {'a':['a','a','a'], 'b':['b','b'], 'a':['a']}
        l_cnt = [(k, len(list(g))) for k, g in groupby(word)]
        res = ''
        for k, cnt in l_cnt:
            qu, rem = divmod(cnt, 9)  # quotient and remainder
            res += ('9' + k) * qu
            if rem: res += str(rem) + k
        return res
