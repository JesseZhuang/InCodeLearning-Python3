"""leet 487, lint 883, medium"""
from collections import deque
from typing import (
    List,
)


class Solution:

    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        """83 ms, 5.28 mb"""
        l, r, k, n = 0, 0, 1, len(nums)
        while r < n:
            k -= nums[r] == 0
            r += 1
            if k < 0:
                k += nums[l] == 0
                l += 1
        return r - l

    def follow_up(selfs, nums: List[int]) -> int:
        """106 ms, 5.08 mb"""
        res, l, r, k, n, q = 0, 0, 0, 1, len(nums), deque()
        while r < n:
            if nums[r] == 0:
                k -= 1
                q.append(r)
            r += 1
            if k < 0:
                l = q.popleft() + 1
                k += 1
            res = max(res, r - l)
        return res
