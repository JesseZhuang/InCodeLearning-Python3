"""leet 1650, medium"""
from jzstruct.tree_node import ParentTreeNode


class Solution:

    def lowestCommonAncestor(self, p: ParentTreeNode, q: ParentTreeNode):
        """lint 801 ms, 7.67 mb"""
        a, b = p, q
        while a != b:
            a = a.parent if a.parent else q
            b = b.parent if b.parent else p
        return a
