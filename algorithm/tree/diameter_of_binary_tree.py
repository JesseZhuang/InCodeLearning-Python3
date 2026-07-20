"""LeetCode 543. Diameter of Binary Tree, easy.
Tags: tree, DFS, binary tree.
"""
from typing import Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """DFS post-order: at each node, diameter through it = left_depth + right_depth.
    Track the global max. Return depth to parent.
    Time O(n), Space O(h) where h is height of the tree."""

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def depth(node: Optional[TreeNode]) -> int:  # O(n) total calls
            if not node:
                return 0
            left = depth(node.left)  # O(h) stack space
            right = depth(node.right)
            self.res = max(self.res, left + right)  # diameter through this node
            return 1 + max(left, right)

        depth(root)
        return self.res
