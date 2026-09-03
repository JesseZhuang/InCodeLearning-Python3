"""leet code 662, medium, tags: binary tree, dfs, bfs."""
from collections import deque
from typing import Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """BFS. O(n) time, O(n) space. 39ms, 17.32mb."""
        q = deque()
        q.append((root, 0))
        res = 0
        while q:
            size = len(q)
            l, r = q[0][1], 0
            for i in range(size):  # O(n) total across all levels
                n, r = q.popleft()
                if n.left is not None: q.append((n.left, 2 * r))
                if n.right is not None: q.append((n.right, 2 * r + 1))
            res = max(res, r - l + 1)
        return res


class Solution2:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """DFS. O(n) time, O(n) space."""
        self.res = 0
        self.left_most = {}

        def dfs(node: Optional[TreeNode], depth: int, pos: int):
            if node is None:
                return
            if depth not in self.left_most:
                self.left_most[depth] = pos
            self.res = max(self.res, pos - self.left_most[depth] + 1)
            dfs(node.left, depth + 1, 2 * pos)  # O(h) stack depth
            dfs(node.right, depth + 1, 2 * pos + 1)

        dfs(root, 0, 0)
        return self.res
