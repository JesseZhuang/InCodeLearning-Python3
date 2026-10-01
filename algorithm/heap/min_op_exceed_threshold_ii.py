"""leet 3066, medium"""
import heapq


class Solution:
    """Min-heap solution, O(n log n) time and O(n) space."""

    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)  # O(n)

        num_operations = 0
        while nums[0] < k:
            x = heapq.heappop(nums)  # O(log n)
            y = heapq.heappop(nums)  # O(log n)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))  # O(log n)

            num_operations += 1

        return num_operations
