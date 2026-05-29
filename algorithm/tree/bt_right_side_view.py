"""LeetCode 199. Binary Tree Right Side View, medium.
Tags: tree, BFS, DFS, binary tree.
"""
from collections import deque
from typing import Optional, List

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """BFS level-order traversal, take last node of each level."""

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:  # O(n) time, O(w) space where w is max width
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == n - 1:  # last node in this level
                    res.append(node.val)
        return res


class Solution2:
    """DFS preorder (root -> right -> left), first node at each new depth."""

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return
            if depth == len(res):  # first visit at this depth
                res.append(node.val)
            dfs(node.right, depth + 1)  # O(n) time, O(h) space
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res
