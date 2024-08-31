"""leet code 759, hard"""


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
