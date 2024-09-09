"""leet code 253, medium"""
from heapq import heappop, heappush
from typing import List

from algorithm.struct.interval import Interval


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        used = []

        for start, end in intervals:
            if used and used[0] <= start:
                heappop(used)
            heappush(used, end)

        return len(used)


class Solution2:
    """
    lint code 919
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)
        used = []

        for i in intervals:
            if used and used[0] <= i.start:
                heappop(used)
            heappush(used, i.end)

        return len(used)
