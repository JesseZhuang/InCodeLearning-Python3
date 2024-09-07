"""leet code 662, medium"""
from collections import deque
from typing import Optional

from algorithm.struct.tree_node import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))
        res = 0
        while q:
            size = len(q)
            left = q[0][1]
            right = left
            for i in range(size):
                cur = q.popleft()
                n, right = cur[0], cur[1]
                if n.left is not None: q.append((n.left, 2 * right))
                if n.right is not None: q.append((n.right, 2 * right + 1))
            res = max(res, right - left + 1)
        return res
