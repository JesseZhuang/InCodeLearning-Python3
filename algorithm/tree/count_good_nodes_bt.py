"""LeetCode 1448. Count Good Nodes in Binary Tree, medium.
Tags: tree, DFS, BFS, binary tree.
"""
from collections import deque
from typing import Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """DFS recursive, track max value from root to current node."""

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], max_so_far: int) -> int:
            if not node:
                return 0
            good = 1 if node.val >= max_so_far else 0  # O(1)
            new_max = max(max_so_far, node.val)
            good += dfs(node.left, new_max)  # O(left subtree)
            good += dfs(node.right, new_max)  # O(right subtree)
            return good  # O(n) time total, O(h) space for recursion stack

        return dfs(root, root.val)


class Solution2:
    """BFS iterative, queue stores (node, max_so_far) pairs."""

    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = deque([(root, root.val)])  # O(w) space where w is max width
        while q:
            node, max_so_far = q.popleft()  # O(1)
            if node.val >= max_so_far:
                count += 1
            new_max = max(max_so_far, node.val)
            if node.left:
                q.append((node.left, new_max))
            if node.right:  # O(n) time total
                q.append((node.right, new_max))
        return count
