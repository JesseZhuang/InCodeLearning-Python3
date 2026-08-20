"""LeetCode 846, medium, tags: array, hash table, greedy, sorting."""
from collections import Counter
import heapq


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        """Greedy with sorted keys: always start a group from the smallest available card.

        Time O(n log n) — sorting dominates; each card is processed once.
        Space O(n) for the counter.
        """
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for start in sorted(count):  # O(n log n)
            if count[start] > 0:
                need = count[start]
                for i in range(start, start + groupSize):  # O(groupSize)
                    if count[i] < need:
                        return False
                    count[i] -= need
        return True


class Solution2:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        """Min-heap approach: pop smallest, try to form a group starting from it.

        Time O(n log n) — heap operations.
        Space O(n) for counter and heap.
        """
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)  # O(n)
        while min_heap:
            start = min_heap[0]  # peek smallest
            for i in range(start, start + groupSize):  # O(groupSize)
                if count[i] == 0:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)  # O(log n)
        return True
