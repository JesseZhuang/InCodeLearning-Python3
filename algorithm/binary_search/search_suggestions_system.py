import bisect


class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        """Sort + binary search. O(n log n + m*L*log n) time, O(sort) space."""
        products.sort()  # O(n log n)
        res = []
        prefix = ""
        for ch in searchWord:  # O(m) iterations
            prefix += ch  # O(L) per append
            lo = bisect.bisect_left(products, prefix)  # O(L * log n)
            suggestions = []
            for i in range(lo, min(lo + 3, len(products))):
                if products[i].startswith(prefix):  # O(L)
                    suggestions.append(products[i])
                else:
                    break
            res.append(suggestions)
        return res


class Solution2:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        """Trie with sorted children. O(n*L) build, O(m*L) query time."""
        root = {}
        products.sort()  # sort so trie insertions maintain order
        for word in products:  # O(n*L) build
            node = root
            for ch in word:  # O(L)
                if ch not in node:
                    node[ch] = {"#": []}
                node = node[ch]
                if len(node["#"]) < 3:
                    node["#"].append(word)

        res = []
        node = root
        for ch in searchWord:  # O(m*L) query
            if node and ch in node:
                node = node[ch]
                res.append(node["#"])
            else:
                node = None
                res.append([])
        return res
