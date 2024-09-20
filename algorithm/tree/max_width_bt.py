"""leet code 662, medium"""
from collections import deque
from typing import Optional

from algorithm.struct.tree_node import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """39ms, 17.32mb"""
        q = deque()
        q.append((root, 0))
        res = 0
        while q:
            size = len(q)
            l, r = q[0][1], 0
            for i in range(size):
                n, r = q.popleft()
                if n.left is not None: q.append((n.left, 2 * r))
                if n.right is not None: q.append((n.right, 2 * r + 1))
            res = max(res, r - l + 1)
        return res
