"""LeetCode 2385. Amount of Time for Binary Tree to Be Infected, medium.
Tags: tree, DFS, BFS, binary tree.
"""
from collections import deque
from typing import Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """Build parent map via DFS, then BFS from start node to find max distance.
    Time O(n), Space O(n)."""

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        start_node = None

        def build(node: Optional[TreeNode], par: Optional[TreeNode]) -> None:  # O(n)
            nonlocal start_node
            if not node:
                return
            parent[node] = par
            if node.val == start:
                start_node = node
            build(node.left, node)
            build(node.right, node)

        build(root, None)

        queue = deque([start_node])
        visited = {start_node}
        minutes = -1
        while queue:  # O(n) total nodes visited
            minutes += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return minutes


class Solution2:
    """Pure DFS: encode distance to start as negative return value.
    Time O(n), Space O(h) where h is tree height."""

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.ans = 0

        def depth(node: Optional[TreeNode]) -> int:  # O(n)
            """Return height of subtree (>=0). If start is found, return -(dist to start)."""
            if not node:
                return 0
            left = depth(node.left)   # O(h) stack depth
            right = depth(node.right)

            if node.val == start:
                # left and right are positive heights of children subtrees
                self.ans = max(self.ans, max(left, right))
                return -1  # 1 edge above start

            if left < 0:  # start is in left subtree, left = -(dist from start to node.left)
                # path going up from start through node then down right subtree
                self.ans = max(self.ans, right - left)
                return left - 1
            if right < 0:  # start is in right subtree
                self.ans = max(self.ans, left - right)
                return right - 1

            return max(left, right) + 1

        depth(root)
        return self.ans
