"""leet code 226, easy, tags: tree, binary tree, dfs, bfs."""
from collections import deque
from typing import Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    # O(n) time, O(h) space where h is tree height (worst case O(n))
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root


class Solution2:
    # O(n) time, O(n) space (queue holds up to n/2 leaf nodes)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return root
