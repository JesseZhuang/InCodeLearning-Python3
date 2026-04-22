"""leet 2452, medium, tags: array, string, trie."""


class Solution:
    """Brute force: compare each query with every dictionary word.

    For each pair, count character mismatches and check if <= 2.
    Time O(q*d*m) where q=len(queries), d=len(dictionary), m=word length.
    Space O(1) extra.
    """

    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        res = []
        for q in queries:
            for d in dictionary:
                if sum(a != b for a, b in zip(q, d)) <= 2:  # O(m) per pair
                    res.append(q)
                    break
        return res


class Solution2:
    """Trie with DFS: build a trie from dictionary, then DFS for each query
    allowing up to 2 mismatches.

    Time O(d*m) to build trie, O(q * 26^2 * m) worst case to query (pruned).
    Space O(d*m) for the trie.
    """

    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        trie: dict = {}
        for word in dictionary:  # O(d*m) build trie
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = True

        def dfs(node: dict, word: str, i: int, edits: int) -> bool:
            if i == len(word):
                return '#' in node
            for ch, child in node.items():
                if ch == '#':
                    continue
                new_edits = edits + (0 if ch == word[i] else 1)
                if new_edits <= 2 and dfs(child, word, i + 1, new_edits):
                    return True
            return False

        return [q for q in queries if dfs(trie, q, 0, 0)]
