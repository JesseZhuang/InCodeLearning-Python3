"""leet 3066, medium"""
import heapq


class Solution:
    """todo editorial"""

    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)

        num_operations = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))

            num_operations += 1

        return num_operations
