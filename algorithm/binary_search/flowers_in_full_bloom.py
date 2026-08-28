from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        """Binary Search on sorted start/end arrays. O((n + q) log n) time, O(n) space.
        At time t, blooming count = (flowers started <= t) - (flowers ended < t)."""
        starts = sorted(s for s, _ in flowers)  # O(n log n)
        ends = sorted(e for _, e in flowers)  # O(n log n)
        res = []
        for t in people:  # O(q) iterations
            started = bisect_right(starts, t)  # O(log n), flowers with start <= t
            ended = bisect_left(ends, t)  # O(log n), flowers with end < t
            res.append(started - ended)
        return res


class Solution2:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        """Sweep Line + Sorted Query Processing. O((n + q) log(n + q)) time, O(n + q) space.
        Use a difference array with events, process queries in sorted order."""
        import heapq
        events = []
        for s, e in flowers:  # O(n)
            events.append((s, 1))   # flower starts blooming
            events.append((e + 1, -1))  # flower stops blooming (day after end)
        events.sort()  # O(n log n)

        indexed_people = sorted(enumerate(people), key=lambda x: x[1])  # O(q log q)
        res = [0] * len(people)
        count = 0
        ei = 0
        for orig_idx, t in indexed_people:  # O(q) iterations
            while ei < len(events) and events[ei][0] <= t:  # amortized O(n) total
                count += events[ei][1]
                ei += 1
            res[orig_idx] = count
        return res
