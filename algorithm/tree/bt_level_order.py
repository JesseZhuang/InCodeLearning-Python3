"""LeetCode 102. Binary Tree Level Order Traversal, medium.
Tags: tree, BFS, DFS, binary tree.
"""
from collections import deque
from typing import Optional, List

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """BFS with queue, process level by level."""

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:  # O(n) time, O(w) space where w is max width
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res


class Solution2:
    """DFS recursive, track depth to place nodes in correct level."""

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return
            if depth == len(res):  # O(n) time, O(h) space
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res
