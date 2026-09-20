"""LeetCode 451, medium, tags: hash table, string, sorting, heap, bucket sort."""
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """HashMap + Sort: count frequencies, sort characters by frequency descending.

        Time O(n + k log k) where k = number of unique chars (at most 62).
        Space O(n) for the result string.
        """
        count = Counter(s)  # O(n)
        chars = sorted(count.keys(), key=lambda c: -count[c])  # O(k log k)
        return ''.join(c * count[c] for c in chars)  # O(n)


class Solution2:
    def frequencySort(self, s: str) -> str:
        """Bucket Sort: use frequency as bucket index, iterate from highest bucket.

        Time O(n), Space O(n).
        """
        count = Counter(s)  # O(n)
        max_freq = max(count.values())  # O(k)
        buckets: list[list[str]] = [[] for _ in range(max_freq + 1)]  # O(n)
        for c, freq in count.items():  # O(k)
            buckets[freq].append(c)
        res = []
        for freq in range(max_freq, 0, -1):  # O(n) total across all buckets
            for c in buckets[freq]:
                res.append(c * freq)
        return ''.join(res)
