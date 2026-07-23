from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """LeetCode 437. Path Sum III. DFS + Prefix Sum HashMap. O(n) time, O(n) space."""

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        self.result = 0

        def dfs(node, curr_sum):
            if not node:
                return
            curr_sum += node.val  # O(1) per node
            self.result += prefix_counts[curr_sum - targetSum]  # O(1) lookup
            prefix_counts[curr_sum] += 1
            dfs(node.left, curr_sum)  # O(n) total across all nodes
            dfs(node.right, curr_sum)
            prefix_counts[curr_sum] -= 1  # backtrack

        dfs(root, 0)
        return self.result


class Solution2:
    """LeetCode 437. Path Sum III. Double DFS brute force. O(n^2) time, O(n) space."""

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return (self._count(root, targetSum)  # O(n) for each starting node
                + self.pathSum(root.left, targetSum)  # O(n) calls total
                + self.pathSum(root.right, targetSum))

    def _count(self, node, remaining):
        if not node:
            return 0
        count = 1 if node.val == remaining else 0
        count += self._count(node.left, remaining - node.val)
        count += self._count(node.right, remaining - node.val)
        return count
