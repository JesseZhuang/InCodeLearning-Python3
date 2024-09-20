"""leet code 890, lint code 1592, medium"""
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """27ms, 16.56mb"""

        def match(w: str) -> bool:
            llm = dict()
            for w, p in zip(w, pattern):
                if llm.setdefault(w, p) != p: return False  # return existing value or new value
                llm[w] = p
            return len(set(llm.values())) == len(llm.values())

        return list(filter(match, words))
