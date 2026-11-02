"""LeetCode 94. Binary Tree Inorder Traversal, easy.

Tags: tree, depth-first search, stack, binary tree.
"""
from typing import List, Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """Iterative DFS using an explicit stack."""

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        # Each node is pushed and popped once: O(n) time, O(h) stack space.
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result


class Solution2:
    """Recursive depth-first traversal."""

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node: Optional[TreeNode]) -> None:
            if not node:
                return
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

        # O(n) time and O(h) call-stack space, where h is tree height.
        traverse(root)
        return result
