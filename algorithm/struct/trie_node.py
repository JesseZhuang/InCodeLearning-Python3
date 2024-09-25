"""
assumptions
1. 26 lower case english letters
2. only insert method needed
3. a variant of this class is no using is_word boolean flag but just save the string at that node
"""


class TrieNode:
    __slots__ = "is_word", "word", "next", "cnt"

    def __init__(self):
        self.is_word = False
        self.word = None
        self.next = dict()  # note used dict, not array of links like in java
        self.cnt = 0

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.next:
                cur.next[c] = TrieNode()
            cur = cur.next[c]
            cur.cnt += 1
        cur.is_word = True  # indentation important cannot be in for loop
        cur.word = word
