"""leet code 2458, hard"""
from typing import Optional, List

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        res = dict()

        def dfs(n: TreeNode | None, d: int, maxH: int):
            if not n:
                return
            res[n.val] = maxH
            dfs(n.left, d + 1, max(maxH, d + 1 + height(n.right)))
            dfs(n.right, d + 1, max(maxH, d + 1 + height(n.left)))

        @cache
        def height(n: TreeNode | None) -> int:
            if not n:
                return -1
            return 1 + max(height(n.left), height(n.right))

        dfs(root, 0, 0)
        return [res[i] for i in queries]
