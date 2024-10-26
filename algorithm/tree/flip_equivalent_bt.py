"""leet code 951, medium"""
from typing import Optional

from algorithm.struct.tree_node import TreeNode


class Solution:
    def flipEquiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if not r1 or not r2:
            return r1 == r2
        return (r1.val == r2.val and  # precedence not>xor>and>or
                (self.flipEquiv(r1.left, r2.left) and self.flipEquiv(r1.right, r2.right) or
                 self.flipEquiv(r1.left, r2.right) and self.flipEquiv(r1.right, r2.left)))
