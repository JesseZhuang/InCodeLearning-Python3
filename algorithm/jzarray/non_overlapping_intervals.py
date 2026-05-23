from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Greedy: sort by end, count overlapping intervals to remove.
        O(n log n) time, O(log n) space (sorting)."""
        intervals.sort(key=lambda x: x[1])  # O(n log n)
        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):  # O(n)
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        return count

    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        """Greedy: sort by start, when overlap keep the one with smaller end.
        O(n log n) time, O(log n) space (sorting)."""
        intervals.sort(key=lambda x: x[0])  # O(n log n)
        count = 0
        pre = 0
        for i in range(1, len(intervals)):  # O(n)
            if intervals[i][0] < intervals[pre][1]:
                count += 1
                if intervals[i][1] < intervals[pre][1]:
                    pre = i
            else:
                pre = i
        return count
