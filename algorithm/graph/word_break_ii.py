"""leet code 140, hard"""
from typing import List


class Solution:

    def __init__(self):
        self.max_l = 0

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = set()
        for w in wordDict:
            self.max_l = max(self.max_l, w)
            d.add(w)
        i_s = dict()  # index -> list of strings for s[index:]
        return self.dfs(s, d, 0, i_s)

    def dfs(self, s, d, start, i_s) -> List[str]:
        if start in i_s: return i_s[start]
        cur = []
        if start == len(s): cur.append("")
        for i in range(start, min(start + self.max_l, len(s))):
            word = s[start:i + 1]
            if word in d:
                next_l = self.dfs(s, d, i + 1, i_s)
                for w in next_l:
                    if not w:
                        cur.append(word)
                    else:
                        cur.append(word + " " + w)
        i_s[start] = cur
        return cur  # list of strings for s[start:]
