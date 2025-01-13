"""leet 2185, easy"""


class Solution:
    """todo editorial"""

    def prefixCount(self, words: list[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)


class Solution2:
    def prefixCount(self, words: list[str], pref: str) -> int:
        trie = self._Trie()

        # Add all words to trie
        for word in words:
            trie._add_word(word)
        return trie._count_prefix(pref)

    class _Trie:
        # Node class represents each character in Trie
        class _Node:
            def __init__(self):
                # Links to child nodes
                self.links = [None] * 26
                # Number of strings having prefix till this node
                self.count = 0

        def __init__(self):
            self.root = self._Node()

        # Add word to trie and update prefix counts
        def _add_word(self, word: str) -> None:
            curr = self.root
            for c in word:
                idx = ord(c) - ord("a")
                if curr.links[idx] is None:
                    curr.links[idx] = self._Node()
                curr = curr.links[idx]
                curr.count += 1  # Increment count for this prefix

        # Return count of strings having pref as prefix
        def _count_prefix(self, pref: str) -> int:
            curr = self.root
            for c in pref:
                idx = ord(c) - ord("a")
                if curr.links[idx] is None:
                    return 0  # Prefix not found
                curr = curr.links[idx]
            return curr.count  # Return count at last node
