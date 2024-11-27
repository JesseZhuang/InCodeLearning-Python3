"""leet code 2583, medium"""
from collections import deque
from heapq import heappush, heappop
from typing import Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        pq, q = list(), deque()
        q.append(root)

        while q:
            size = len(q)
            sum = 0
            while size > 0:
                n = q.popleft()
                sum += n.val
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
                size -= 1
            heappush(pq, sum)
            if len(pq) > k: heappop(pq)
        if len(pq) < k: return -1
        return pq[0]
