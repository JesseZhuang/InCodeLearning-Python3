"""leet 981, medium, tags: hash table, string, binary search, design."""
from bisect import bisect_right
from collections import defaultdict


class TimeMap:
    """Hash map + binary search. set: O(1), get: O(log n) time, O(n) space overall."""

    def __init__(self):
        self.store: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))  # O(1) amortized

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        vals = self.store[key]
        i = bisect_right(vals, (timestamp, chr(127)))  # O(log n)
        return vals[i - 1][1] if i > 0 else ""


class TimeMap2:
    """Hash map + linear scan from end (simpler, for small n). set: O(1), get: O(n) time."""

    def __init__(self):
        self.store: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        vals = self.store[key]
        # O(n): scan from end to find largest timestamp <= given
        for i in range(len(vals) - 1, -1, -1):
            if vals[i][0] <= timestamp:
                return vals[i][1]
        return ""
