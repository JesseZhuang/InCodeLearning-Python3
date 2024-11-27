"""leet code 106, medium"""
from typing import List, Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.root_id = len(postorder) - 1
        val_ind = dict()
        for i, v in enumerate(inorder): val_ind[v] = i

        def dfs(l: int, r: int) -> Optional[TreeNode]:
            if l > r: return None
            root = postorder[self.root_id]
            self.root_id -= 1
            n = TreeNode(root)
            mid = val_ind[root]
            n.right = dfs(mid + 1, r)
            n.left = dfs(l, mid - 1)
            return n

        return dfs(0, len(inorder) - 1)
