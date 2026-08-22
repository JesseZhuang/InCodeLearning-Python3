"""leet 528, medium, tags: prefix sum, binary search, randomized, math."""
import random
from bisect import bisect_left


class Solution:
    """Prefix sum + binary search. __init__: O(n) time, O(n) space. pickIndex: O(log n) time."""

    def __init__(self, w: list[int]):
        self.prefix = []
        total = 0
        for weight in w:  # O(n)
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect_left(self.prefix, target)  # O(log n)


class Solution2:
    """Prefix sum + linear scan. __init__: O(n) time, O(n) space. pickIndex: O(n) time."""

    def __init__(self, w: list[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        for i, val in enumerate(self.prefix):  # O(n)
            if target <= val:
                return i
        return len(self.prefix) - 1
