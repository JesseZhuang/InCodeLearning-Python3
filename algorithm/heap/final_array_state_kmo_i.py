"""leet 3264, easy"""
from heapq import heapify, heappop, heappush


class Solution:
    """todo editorial"""

    def getFinalState(self, nums: list[int], k: int, multiplier: int):
        pq = [(val, i) for i, val in enumerate(nums)]
        heapify(pq)

        for _ in range(k):
            _, i = heappop(pq)
            nums[i] *= multiplier
            heappush(pq, (nums[i], i))

        return nums
