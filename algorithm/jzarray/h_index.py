"""Solutions for LeetCode 274, H-Index."""


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """Count papers by citation count, capped at the number of papers.

        Time O(n): each paper is counted once and each bucket is checked once.
        Space O(n): the bucket array has n + 1 entries.
        """
        n = len(citations)
        buckets = [0] * (n + 1)
        for count in citations:  # O(n) total work
            buckets[min(count, n)] += 1

        papers = 0
        for h in range(n, -1, -1):  # O(n) total work
            papers += buckets[h]
            if papers >= h:
                return h
        return 0

    def hIndexSort(self, citations: list[int]) -> int:
        """Sort citations descending and find the largest valid prefix.

        Time O(n log n) for sorting; the scan is O(n).
        Space O(n) for the sorted copy.
        """
        ordered = sorted(citations, reverse=True)
        for index, count in enumerate(ordered, start=1):  # O(n) scan
            if count < index:
                return index - 1
        return len(ordered)
