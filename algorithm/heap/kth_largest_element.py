"""leet 215, medium"""
import heapq
import random


class Solution:
    """Min-heap approach, O(n log k) time, O(k) space."""

    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:  # O(n)
            heapq.heappush(heap, num)  # O(log k)
            if len(heap) > k:
                heapq.heappop(heap)  # O(log k)
        return heap[0]


class Solution2:
    """Quickselect approach, O(n) average time, O(1) space."""

    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k  # kth largest = (n-k)th smallest in 0-indexed
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            pivot_idx = random.randint(lo, hi)
            pivot_idx = self._partition(nums, lo, hi, pivot_idx)
            if pivot_idx == target:
                return nums[pivot_idx]
            elif pivot_idx < target:
                lo = pivot_idx + 1  # search right half
            else:
                hi = pivot_idx - 1  # search left half
        return -1  # unreachable

    @staticmethod
    def _partition(nums: list[int], lo: int, hi: int, pivot_idx: int) -> int:
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[hi] = nums[hi], nums[pivot_idx]  # move pivot to end
        store = lo
        for i in range(lo, hi):  # O(hi - lo)
            if nums[i] < pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        nums[store], nums[hi] = nums[hi], nums[store]  # place pivot in final position
        return store
