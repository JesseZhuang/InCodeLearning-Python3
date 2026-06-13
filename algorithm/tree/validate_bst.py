"""LeetCode 98 medium, tags: tree, depth-first search, binary search tree, binary tree."""

from math import inf

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: 'TreeNode') -> bool:
        """Recursive DFS with min/max bounds. O(n) time, O(h) space."""
        return self._valid(root, -inf, inf)

    def _valid(self, node, lo, hi):
        if not node:
            return True
        if node.val <= lo or node.val >= hi:  # O(1)
            return False
        return self._valid(node.left, lo, node.val) and self._valid(node.right, node.val, hi)


class Solution2:
    def isValidBST(self, root: 'TreeNode') -> bool:
        """Iterative inorder traversal. O(n) time, O(h) space."""
        stack, prev = [], -inf
        cur = root
        while cur or stack:
            while cur:  # O(h) go to leftmost
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val <= prev:  # O(1) check ascending order
                return False
            prev = cur.val
            cur = cur.right
        return True
