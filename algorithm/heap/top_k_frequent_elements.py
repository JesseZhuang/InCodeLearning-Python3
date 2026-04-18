"""leet 347, medium, tags: array, hash table, divide and conquer, sorting, heap, bucket sort, counting, quickselect."""
from collections import Counter
from heapq import heappush, heappop


class Solution:
    """bucket sort. O(n) time, O(n) space."""

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        n = len(nums)
        buckets: list[list[int]] = [[] for _ in range(n + 1)]  # O(n) space
        for num, freq in count.items():  # O(n) distribute to buckets
            buckets[freq].append(num)
        res = []
        for freq in range(n, 0, -1):  # O(n) collect from highest freq
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


class Solution2:
    """min-heap of size k. O(n log k) time, O(n) space."""

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)  # O(n) time and space
        heap: list[tuple[int, int]] = []
        for num, freq in count.items():  # O(n log k): iterate n unique, each heap op log k
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)  # evict least frequent
        return [num for _, num in heap]
