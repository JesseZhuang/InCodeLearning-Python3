"""LeetCode 373, medium, tags: array, heap."""
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """Min-heap approach. Push (nums1[i] + nums2[0], i, 0) for first min(k, len(nums1)) rows,
        then pop and advance column index.

        Time O(k log k), Space O(k).
        """
        if not nums1 or not nums2:
            return []
        res = []
        heap = []
        for i in range(min(k, len(nums1))):  # O(k) initial entries
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        while heap and len(res) < k:  # O(k) pops, each O(log k)
            total, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res

    def kSmallestPairsBFS(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """BFS-like expansion with visited set. Start from (0,0), expand right and down.

        Time O(k log k), Space O(k).
        """
        if not nums1 or not nums2:
            return []
        res = []
        visited = {(0, 0)}
        heap = [(nums1[0] + nums2[0], 0, 0)]
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
