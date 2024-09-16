"""
assumptions
1. 26 lower case english letters
2. only insert method needed
3. a variant of this class is no using is_word boolean flag but just save the string at that node
"""


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.word = None
        self.next = {}  # note used dict, not array of links like in java

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.next:
                cur.next[c] = TrieNode()
            cur = cur.next[c]
        cur.is_word = True  # indentation important cannot be in for loop
        cur.word = word
