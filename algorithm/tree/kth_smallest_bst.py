"""LeetCode 230 medium, tags: tree, depth-first search, binary search tree, binary tree."""

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    def kthSmallest(self, root: 'TreeNode', k: int) -> int:
        """Iterative inorder traversal with stack. O(H+k) time, O(H) space."""
        stack = []
        cur = root
        while cur or stack:
            while cur:  # O(H) go to leftmost
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:  # found kth smallest
                return cur.val
            cur = cur.right
