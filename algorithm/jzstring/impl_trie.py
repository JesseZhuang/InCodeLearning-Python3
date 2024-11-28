"""leet code 208, medium, 133ms, 31.6mb"""
from typing import Optional, Self


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.next = dict()  # note used dict, not array of links like in java

    def get(self, word: str) -> Optional[Self]:
        cur = self
        for c in word:
            if c not in cur.next: return None
            cur = cur.next[c]
        return cur

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.next:  # can use defaultdict(dict), then if not cur.next[c]:
                cur.next[c] = TrieNode()
            cur = cur.next[c]
        cur.is_word = True  # indentation important cannot be in for loop


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        self.root.insert(word)

    def search(self, word: str) -> bool:
        n = self.get(word)
        return n is not None and n.is_word  # n and n.is_word -> None when n is None, not boolean

    def startsWith(self, prefix: str) -> bool:
        n = self.get(prefix)
        return n is not None

    def get(self, word: str) -> Optional[TrieNode]:
        return self.root.get(word)


if __name__ == "__main__":
    trie = Trie()
    print(trie.search("a"))
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.startsWith("app"))
