"""leet code 1438, medium, sliding window + monotonic deques"""

from collections import deque
from typing import List
from sortedcontainers import SortedList


class Solution:
    """Monotonic deques: O(n) time, O(n) space"""

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq, min_dq = deque(), deque()  # O(n) space for both deques
        l = 0
        res = 0
        for r, n in enumerate(nums):  # O(n) outer loop
            while max_dq and n >= nums[max_dq[-1]]:
                max_dq.pop()
            while min_dq and n <= nums[min_dq[-1]]:
                min_dq.pop()
            max_dq.append(r)
            min_dq.append(r)
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:  # amortized O(1)
                l += 1
                if max_dq[0] < l:
                    max_dq.popleft()
                if min_dq[0] < l:
                    min_dq.popleft()
            res = max(res, r - l + 1)
        return res


class Solution2:
    """Sorted list (balanced BST): O(n log n) time, O(n) space"""

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sl = SortedList()  # O(n) space
        l = 0
        res = 0
        for r, n in enumerate(nums):  # O(n) outer loop
            sl.add(n)  # O(log n) per insertion
            while sl[-1] - sl[0] > limit:
                sl.remove(nums[l])  # O(log n) per removal
                l += 1
            res = max(res, r - l + 1)
        return res
