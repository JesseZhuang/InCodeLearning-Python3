"""leet code 759, hard"""
from typing import List


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Flattening the schedule
        intervals = [interval for employee in schedule for interval in employee]
        # Sorting by start of each Interval
        intervals.sort(key=lambda x: x.start)
        res, end = [], intervals[0].end
        # Checking for free time between intervals
        for i in intervals[1:]:
            if end < i.start:
                res.append(Interval(end, i.start))
            end = max(end, i.end)
        return res


class SolutionLint:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals
    """

    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        # 81ms, 6.23Mb lint code
        intervals = []
        for s in schedule:
            for i in range(len(s) // 2):
                intervals.append(Interval(s[2 * i], s[2 * i + 1]))
        intervals.sort(key=lambda x: x.start)
        end = intervals[0].end
        res = []
        for i in intervals[1:]:
            if end < i.start:
                res.append(Interval(end, i.start))
            end = max(end, i.end)
        return res
