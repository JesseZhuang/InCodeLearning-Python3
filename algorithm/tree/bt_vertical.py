"""leet code 314, lint code 651, medium"""
from collections import defaultdict, deque
from typing import List

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """lint code, 81 ms, 5.01 mb"""

    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        col_nodes = defaultdict(list)
        min_c, max_c, q = 0, 0, deque()
        q.append((root, 0))
        while q:
            n, c = q.popleft()
            col_nodes[c].append(n.val)
            max_c, min_c = max(max_c, c), min(min_c, c)
            if n.left:
                q.append((n.left, c - 1))
            if n.right:
                q.append((n.right, c + 1))
        for i in range(min_c, max_c + 1):
            res.append(col_nodes[i])
        return res
