"""LeetCode 1696, medium: dynamic programming with a sliding maximum."""

from collections import deque
from heapq import heappop, heappush


class Solution:
    """Monotonic deque, O(n) time and O(k) auxiliary space."""

    def maxResult(self, nums: list[int], k: int) -> int:
        candidates = deque([(0, nums[0])])
        score = nums[0]

        for index in range(1, len(nums)):  # O(n) indices are added once.
            while candidates[0][0] < index - k:
                candidates.popleft()
            score = nums[index] + candidates[0][1]
            while candidates and candidates[-1][1] <= score:
                candidates.pop()  # O(n) total removals across the outer loop.
            candidates.append((index, score))

        return score


class Solution2:
    """Max-heap with lazy expiry, O(n log n) time and O(n) space."""

    def maxResult(self, nums: list[int], k: int) -> int:
        candidates = [(-nums[0], 0)]
        score = nums[0]

        for index in range(1, len(nums)):  # O(n) heap pushes and pops in total.
            while candidates[0][1] < index - k:
                heappop(candidates)
            score = nums[index] - candidates[0][0]
            heappush(candidates, (-score, index))  # O(log n) per heap operation.

        return score
