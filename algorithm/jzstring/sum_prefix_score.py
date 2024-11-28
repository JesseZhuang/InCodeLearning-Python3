"""leet code 2416, hard"""
from algorithm.jzstruct.trie_node import TrieNode


class Solution:
    """1512ms, 259,51mb"""

    def __init__(self):
        self.root = TrieNode()

    # Calculate the prefix count using this function.
    def count(self, s: str) -> int:
        cur = self.root
        res = 0
        # The res would store the total sum of counts.
        for c in s:
            cur = cur.next[c]
            res += cur.cnt
        return res

    def sumPrefixScores(self, words):
        for w in words: self.root.insert(w)
        return [self.count(w) for w in words]
