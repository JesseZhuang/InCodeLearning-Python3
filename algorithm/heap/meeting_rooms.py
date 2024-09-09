"""leet code 252, lint code 920, easy"""
from typing import List

from algorithm.struct.interval import Interval


class Solution1:
    """leet code"""

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]: return False
        return True


class Solution2:
    """
    lint code 920
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda e: e.start)  # must have key, otherwise < not supported
        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False
        return True
