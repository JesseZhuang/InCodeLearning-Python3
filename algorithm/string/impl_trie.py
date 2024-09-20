"""leet code 208, medium, 133ms, 31.6mb"""
from typing import Optional


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.next = {}  # note used dict, not array of links like in java


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.next:  # can use defaultdict(dict), then if not cur.next[c]:
                cur.next[c] = TrieNode()
            cur = cur.next[c]
        cur.is_word = True  # indentation important cannot be in for loop

    def search(self, word: str) -> bool:
        n = self.get(word)
        return n and n.is_word

    def startsWith(self, prefix: str) -> bool:
        n = self.get(prefix)
        return n is not None

    def get(self, word: str) -> Optional[TrieNode]:
        cur = self.root
        for c in word:
            if c not in cur.next: return None
            cur = cur.next[c]
        return cur


if __name__ == "__main__":
    print("start")
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.startsWith("app"))
