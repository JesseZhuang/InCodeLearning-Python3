"""leet 2415, medium"""
from jzstruct.tree_node import TreeNode


class Solution:
    """11 ms, 22.92 mb"""

    def reverseOddLevels(self, root) -> TreeNode:
        def dfs(l, r, d):
            if l is None or r is None: return
            if d % 2 == 1: l.val, r.val = r.val, l.val
            dfs(l.left, r.right, d + 1)
            dfs(l.right, r.left, d + 1)

        dfs(root.left, root.right, 1)
        return root
