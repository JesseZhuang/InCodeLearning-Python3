"""leet 692, medium, tags: hash table, string, trie, sorting, heap, bucket sort, counting."""
from collections import Counter
from heapq import heappush, heappop


class Solution:
    """min-heap of size k. O(n log k) time, O(n) space."""

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)  # O(n) time and space
        heap: list[tuple[int, str]] = []
        for word, freq in count.items():  # O(n log k): iterate n unique, each heap op log k
            heappush(heap, (-freq, word))  # negate freq for max-heap behavior
        res = []
        for _ in range(k):  # O(k log n)
            res.append(heappop(heap)[1])
        return res


class Solution2:
    """bucket sort. O(n) time for counting and bucketing, O(m log m) for sorting within buckets."""

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)  # O(n) time and space
        n = len(words)
        buckets: list[list[str]] = [[] for _ in range(n + 1)]  # O(n) space, index = frequency
        for word, freq in count.items():  # O(m) distribute, m unique words
            buckets[freq].append(word)
        res = []
        for freq in range(n, 0, -1):  # O(n) collect from highest freq
            bucket = sorted(buckets[freq])  # sort lexicographically within same frequency
            for word in bucket:
                res.append(word)
                if len(res) == k:
                    return res
        return res
