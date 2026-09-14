"""LeetCode 572. Subtree of Another Tree, easy.
Tags: tree, dfs, string matching, binary tree, hash function.
"""
from typing import Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """Recursive DFS: for each node in root, check if subtree matches subRoot.
    Time O(m*n) worst case, Space O(m) recursion stack."""

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return subRoot is None
        return self._same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def _same(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:  # O(min(m,n))
        if a is None or b is None:
            return a is b
        return a.val == b.val and self._same(a.left, b.left) and self._same(a.right, b.right)


class Solution2:
    """Serialization: serialize both trees with boundary markers, check substring.
    Time O(m+n), Space O(m+n)."""

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node: Optional[TreeNode]) -> str:
            if node is None:
                return "#"
            return f",{node.val}," + serialize(node.left) + "," + serialize(node.right)  # O(n) nodes

        return serialize(subRoot) in serialize(root)  # O(m+n) with built-in string search
