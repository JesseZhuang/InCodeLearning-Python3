"""LeetCode 337. House Robber III, medium.
Tags: tree, DFS, dynamic programming, binary tree.
"""
from typing import Optional, Tuple

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """Post-order DFS returning (rob_this, skip_this) for each node.
    If we rob this node: gain = val + skip_left + skip_right.
    If we skip this node: gain = max(rob_left, skip_left) + max(rob_right, skip_right).
    Time O(n), Space O(h) where h is the height of the tree."""

    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:  # O(n) total calls
            if not node:
                return 0, 0
            left = dfs(node.left)  # O(h) stack space
            right = dfs(node.right)
            rob_this = node.val + left[1] + right[1]
            skip_this = max(left) + max(right)
            return rob_this, skip_this

        return max(dfs(root))
