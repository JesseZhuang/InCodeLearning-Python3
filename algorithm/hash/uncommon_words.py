"""leet code 884, easy"""
from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """43ms, 16.7mb"""
        counts = Counter((s1 + " " + s2).split(" "))

        res = []
        for w, cnt in counts.items():
            if cnt == 1: res.append(w)
        return res
