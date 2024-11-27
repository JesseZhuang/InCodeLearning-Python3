"""leet code 2641, medium"""
from collections import defaultdict
from typing import Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l_sum = defaultdict(int)

        def level_sum(n: Optional[TreeNode], level: int) -> None:
            if not n:
                return
            l_sum[level] += n.val
            level_sum(n.left, level + 1)
            level_sum(n.right, level + 1)

        def update(n: Optional[TreeNode], level: int, sibling: int) -> None:
            if not n:
                return
            left = n.left.val if n.left else 0
            right = n.right.val if n.right else 0
            if level == 0 or level == 1:
                n.val = 0
            else:
                n.val = l_sum[level] - sibling - n.val
            update(n.left, level + 1, right)
            update(n.right, level + 1, left)

        level_sum(root, 0)
        update(root, 0, 0)
        return root
