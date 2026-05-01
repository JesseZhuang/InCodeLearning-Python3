"""LeetCode 862, hard, tags: array, queue, sliding window, heap, monotonic queue, binary search, prefix sum."""
from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """O(n) time, O(n) space."""
        n = len(nums)
        res = n + 1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        dq = deque()
        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                res = min(res, i - dq.popleft())
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)
        return res if res <= n else -1
