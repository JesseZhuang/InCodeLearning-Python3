"""leet code 140, hard"""
from typing import List

from algorithm.jzstruct.trie_node import TrieNode


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = set()
        max_l = 0
        for w in wordDict:
            max_l = max(max_l, w)
            d.add(w)
        i_s = dict()  # index -> list of strings for s[index:]

        def dfs(start: int) -> List[str]:
            if start in i_s: return i_s[start]
            cur = []
            if start == len(s): cur.append("")
            for i in range(start + 1, min(start + max_l, len(s))):
                word = s[start:i]
                if word in d:
                    next_l = dfs(i)
                    for w in next_l:
                        if not w:
                            cur.append(word)
                        else:
                            cur.append(word + " " + w)
            i_s[start] = cur
            return cur  # list of strings for s[start:]

        return dfs(0)


class SolutionTrie:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = TrieNode()
        for w in wordDict: root.insert(w)
        cache = dict()  # index->[sentences]
        for start in range(len(s) - 1, -1, -1):
            sentences = []
            cur = root
            for end in range(start, len(s)):
                c = s[end]
                if c not in cur.next: break
                cur = cur.next[c]
                if cur.is_word:
                    cw = s[start:end + 1]
                    if end == len(s) - 1:
                        sentences.append(cw)
                    else:
                        for sentence in cache.get(end + 1):
                            sentences.append(cw + " " + sentence)
            cache[start] = sentences
        return cache.get(0, [])
