"""leet code 2707, medium"""
from typing import List

from algorithm.jzstruct.trie_node import TrieNode


class Solution:
    """156ms, 17.27mb"""

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = TrieNode()
        for w in dictionary: root.insert(w)
        dp = [0] * (n + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            cur = root
            for end in range(start, n):
                if s[end] not in cur.next: break
                cur = cur.next[s[end]]
                if cur.is_word: dp[start] = min(dp[start], dp[end + 1])

        return dp[0]
