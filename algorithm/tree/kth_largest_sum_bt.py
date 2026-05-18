"""LeetCode 2583, medium, tags: tree, breadth-first search, sorting, binary tree."""
from collections import deque
from typing import Optional
import heapq

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """BFS level-order + sort. O(n) time for BFS, O(d log d) for sort where d = depth."""

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        level_sums = []
        queue = deque([root])  # O(w) space, w = max width
        while queue:
            level_sum = 0
            for _ in range(len(queue)):  # O(n) total across all levels
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sums.append(level_sum)
        if k > len(level_sums):
            return -1
        level_sums.sort(reverse=True)  # O(d log d)
        return level_sums[k - 1]


class Solution2:
    """BFS + min-heap of size k. O(n) time for BFS, O(k) space for heap."""

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        heap = []  # O(k) space
        queue = deque([root])
        while queue:
            level_sum = 0
            for _ in range(len(queue)):  # O(n) total
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(heap) < k:
                heapq.heappush(heap, level_sum)  # O(log k)
            elif level_sum > heap[0]:
                heapq.heapreplace(heap, level_sum)  # O(log k)
        if len(heap) < k:
            return -1
        return heap[0]
