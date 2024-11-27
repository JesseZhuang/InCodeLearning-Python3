"""leet code 314, lint code 651, medium"""
from collections import defaultdict, deque
from typing import List

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """
    lint code, 81ms, 5.01mb
    @param root: the root of tree
    @return: the vertical order traversal
    """

    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if not root: return []
        col_nodes = defaultdict(list)
        q = deque()
        q.append((root, 0))
        min_c = max_c = 0
        while q:
            node, col = q.popleft()
            col_nodes[col].append(node.val)
            max_c = max(max_c, col)
            min_c = min(min_c, col)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        res = []
        for i in range(min_c, max_c + 1):
            res.append(col_nodes[i])
        return res
