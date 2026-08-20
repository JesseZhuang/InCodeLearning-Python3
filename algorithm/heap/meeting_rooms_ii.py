"""LeetCode 253, medium, tags: heap, sweep line, sorting."""
from heapq import heappop, heappush
from typing import List


class Solution:
    """Min-heap approach. O(n log n) time, O(n) space."""

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()  # O(n log n)
        used = []

        for start, end in intervals:  # O(n)
            if used and used[0] <= start:
                heappop(used)  # O(log n)
            heappush(used, end)  # O(log n)

        return len(used)


class Solution2:
    """Sweep line: sort starts and ends separately. O(n log n) time, O(n) space."""

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)  # O(n log n)
        ends = sorted(i[1] for i in intervals)  # O(n log n)
        rooms, end_ptr = 0, 0

        for i in range(len(intervals)):  # O(n)
            if starts[i] < ends[end_ptr]:
                rooms += 1
            else:
                end_ptr += 1

        return rooms
