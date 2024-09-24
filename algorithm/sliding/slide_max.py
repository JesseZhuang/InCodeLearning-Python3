"""leet code 239, hard"""

from collections import deque
from typing import List


class Solution:
    """1113ms, 32.3mb"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        for i, n in enumerate(nums):
            if dq and dq[0] < i - (k - 1): dq.popleft()
            while dq and n >= nums[dq[-1]]: dq.pop()
            dq.append(i)
            if i >= k - 1: res.append(nums[dq[0]])
        return res
