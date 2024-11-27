"""leet code 124, hard"""
from typing import Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1 << 31

        def maxGain(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node: return 0
            left = max(0, maxGain(node.left))
            right = max(0, maxGain(node.right))
            res = max(res, left + right + node.val)
            return max(left, right) + node.val

        if not root: return 0
        maxGain(root)
        return res
