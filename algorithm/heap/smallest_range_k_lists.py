"""leet code 632, hard"""
import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = [(row[0], r, 0) for r, row in enumerate(nums)]  # first element of tuple should be key
        heapq.heapify(pq)

        left, right = -1e9, 1e9
        max_v = max(row[0] for row in nums)
        while pq:
            v, r, c = heapq.heappop(pq)
            if max_v - v < right - left:
                right = max_v
                left = v
            if c + 1 == len(nums[r]): return [left, right]
            v = nums[r][c + 1]
            max_v = max(max_v, v)
            heapq.heappush(pq, (v, r, c + 1))
