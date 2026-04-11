"""leet 56, medium, tags: array, sorting."""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()  # O(n log n), sort by start then end
        res = [intervals[0]]
        for start, end in intervals[1:]:  # O(n)
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res  # Time O(n log n), Space O(n)
