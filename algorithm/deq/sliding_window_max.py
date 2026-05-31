from collections import deque


class Solution:
    """LeetCode 239. Sliding Window Maximum. Monotonic deque approach."""

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        dq = deque()  # stores indices, front is always the max in window
        for i, v in enumerate(nums):  # O(n)
            if dq and dq[0] < i - (k - 1):
                dq.popleft()
            while dq and nums[dq[-1]] <= v:  # O(1) amortized, each element pushed/popped at most once
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res  # O(n) time, O(k) space


class Solution2:
    """Brute force with max() for comparison. O(n*k) time, O(1) extra space."""

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]  # O(n*k)
