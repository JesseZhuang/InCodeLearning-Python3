"""LeetCode 452, medium, tags: array, greedy, sorting."""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """Sort by end coordinate, greedily shoot at each balloon's end.
        O(n log n) time, O(log n) space (sorting)."""
        points.sort(key=lambda x: x[1])  # O(n log n)
        arrows = 1
        end = points[0][1]
        for i in range(1, len(points)):  # O(n)
            if points[i][0] > end:
                arrows += 1
                end = points[i][1]
        return arrows

    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        """Sort by start coordinate, merge overlapping balloons.
        O(n log n) time, O(log n) space (sorting)."""
        points.sort(key=lambda x: x[0])  # O(n log n)
        arrows = 1
        end = points[0][1]
        for i in range(1, len(points)):  # O(n)
            if points[i][0] <= end:
                end = min(end, points[i][1])
            else:
                arrows += 1
                end = points[i][1]
        return arrows
