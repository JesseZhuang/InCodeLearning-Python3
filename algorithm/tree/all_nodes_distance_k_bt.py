"""LeetCode 863. All Nodes Distance K in Binary Tree, medium.
Tags: tree, DFS, BFS, binary tree.
"""
from collections import deque
from typing import List, Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """Build parent map via DFS, then BFS from target for K levels.
    Time O(n), Space O(n)."""

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def build_parent(node: TreeNode, par: Optional[TreeNode]) -> None:  # O(n)
            if not node:
                return
            parent[node] = par
            build_parent(node.left, node)
            build_parent(node.right, node)

        build_parent(root, None)

        queue = deque([target])
        visited = {target}
        dist = 0
        while queue:
            if dist == k:
                return [node.val for node in queue]  # O(n) worst case
            dist += 1
            for _ in range(len(queue)):  # O(n) total across all levels
                node = queue.popleft()
                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return []


class Solution2:
    """Pure DFS: find target, then collect nodes at remaining distance in subtrees.
    Time O(n), Space O(n)."""

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []

        def collect(node: Optional[TreeNode], dist: int) -> None:  # O(n) total
            if not node or dist > k:
                return
            if dist == k:
                res.append(node.val)
                return
            collect(node.left, dist + 1)  # O(h) stack
            collect(node.right, dist + 1)

        def dfs(node: Optional[TreeNode]) -> int:  # O(n)
            """Return distance from node to target, or -1 if target not in subtree."""
            if not node:
                return -1
            if node is target:
                collect(node, 0)
                return 0
            left = dfs(node.left)
            if left >= 0:
                if left + 1 == k:
                    res.append(node.val)
                else:
                    collect(node.right, left + 2)  # distance from right child to target
                return left + 1
            right = dfs(node.right)
            if right >= 0:
                if right + 1 == k:
                    res.append(node.val)
                else:
                    collect(node.left, right + 2)
                return right + 1
            return -1

        dfs(root)
        return res
