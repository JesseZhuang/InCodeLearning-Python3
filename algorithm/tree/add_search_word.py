"""LeetCode 211, medium, tags: string, dfs, design, trie."""


class WordDictionary:
    """Trie + DFS. addWord O(L), search O(L) avg, O(26^L) worst with wildcards. Space O(N*L)."""

    def __init__(self):
        self.children: dict[str, 'WordDictionary'] = {}
        self.is_word = False

    def addWord(self, word: str) -> None:
        node = self
        for c in word:  # O(L)
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self._match(word, 0)

    def _match(self, word: str, i: int) -> bool:
        if i == len(word):
            return self.is_word
        c = word[i]
        if c != '.':
            return c in self.children and self.children[c]._match(word, i + 1)
        return any(child._match(word, i + 1) for child in self.children.values())  # O(26) per dot


class WordDictionaryMap:
    """HashMap by length, brute-force match. addWord O(1), search O(N*L). Space O(N*L)."""

    def __init__(self):
        self.words: dict[int, list[str]] = {}

    def addWord(self, word: str) -> None:  # O(1)
        self.words.setdefault(len(word), []).append(word)

    def search(self, word: str) -> bool:
        for s in self.words.get(len(word), []):  # O(N) words of same length
            if all(wc == '.' or wc == sc for wc, sc in zip(word, s)):  # O(L)
                return True
        return False
