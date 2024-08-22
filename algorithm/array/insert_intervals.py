'''leet code 57 medium'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, l = 0, len(intervals)
        while i < l and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < l and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)
        while i < l:
            res.append(intervals[i])
            i += 1
        return res
