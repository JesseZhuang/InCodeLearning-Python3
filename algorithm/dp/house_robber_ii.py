'''leetcode 213'''

from typing import List


def rob(nums: List[int]) -> int:
    '''dp O(n) time, O(1) space, 42ms, 13.8Mb'''
    def simple_rob(nums, i, j) -> int:
        robbed, did_not_rob_prev = 0, 0
        for idx in range(i, j):
            robbed, did_not_rob_prev = did_not_rob_prev + nums[idx], max(did_not_rob_prev, robbed)
        return max(robbed, did_not_rob_prev)
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    return max(simple_rob(nums, 0, len(nums) - 1), simple_rob(nums, 1, len(nums)))
