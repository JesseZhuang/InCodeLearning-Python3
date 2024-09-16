"""leet code 239, hard"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        for i, n in enumerate(nums):
            if q and q[0] < i - (k - 1): q.popleft()
            while q and n >= nums[q[-1]]: q.pop()
            q.append(i)
            if i >= k - 1: res.append(nums[q[0]])
        return res
