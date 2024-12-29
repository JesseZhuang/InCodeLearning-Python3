"""leet 515, medium"""
from typing import Optional

from jzstruct.tree_node import TreeNode


class Solution:
    """todo editorial"""

    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(node, depth):
            if not node:
                return

            if depth == len(ans):
                ans.append(node.val)
            else:
                ans[depth] = max(ans[depth], node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        ans = []
        dfs(root, 0)
        return ans
