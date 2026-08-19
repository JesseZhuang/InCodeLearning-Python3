"""leet code 45, medium, tags: array, dp, greedy."""
from typing import List


class Solution:
    """Greedy. O(n) time, O(1) space. 109ms, 17.59mb."""

    def jump(self, nums: List[int]) -> int:
        i, p, reach, res = 0, 0, 0, 0
        while p < len(nums) - 1:  # O(n)
            reach = max(reach, i + nums[i])
            if i == p:
                p = reach
                res += 1
            i += 1
        return res


class Solution2:
    """BFS level-order. O(n) time, O(1) space."""

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        level, cur_end, nxt_end = 0, 0, 0
        for i in range(n - 1):  # O(n)
            nxt_end = max(nxt_end, i + nums[i])
            if i == cur_end:
                level += 1
                cur_end = nxt_end
                if cur_end >= n - 1:
                    break
        return level
