"""LeetCode 114. Flatten Binary Tree to Linked List, medium.
Tags: tree, depth-first search, linked list, stack, binary tree.
"""
from typing import Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """Iterative O(n) time, O(1) space. For each node, find the rightmost
    node in the left subtree, link it to the right subtree, then move
    left subtree to right."""

    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:  # O(n) — each node visited at most twice
            if cur.left:
                rightmost = cur.left
                while rightmost.right:  # find rightmost of left subtree
                    rightmost = rightmost.right
                rightmost.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right


class Solution2:
    """Recursive reverse postorder (right, left, root). O(n) time, O(h) space."""

    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None
        self._flatten(root)

    def _flatten(self, node: Optional[TreeNode]) -> None:
        if not node:
            return
        self._flatten(node.right)  # process right first
        self._flatten(node.left)
        node.right = self.prev
        node.left = None
        self.prev = node
