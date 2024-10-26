"""leet code 890, lint code 1592, medium"""
from typing import List


class Solution:
    """27ms, 16.56mb"""

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str) -> bool:
            llm = dict()
            for w, p in zip(word, pattern):
                if llm.setdefault(w, p) != p: return False
                # setdefault() return existing value if key exist, do not change dict
                # otherwise set with the specified default and returns that default
            return len(set(llm.values())) == len(llm.values())

        return list(filter(match, words))
