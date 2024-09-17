"""leet code 287, medium"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """481ms, 30.8mb"""  # nums: [1,3,4,2,2]
        slow, fast = 0, 0
        while True:  # 1,3->3,4->2,4->4,4
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        slow = 0
        while slow != fast:  # 0,4 ->1,2->3,4->2,2
            slow = nums[slow]
            fast = nums[fast]
        return slow
