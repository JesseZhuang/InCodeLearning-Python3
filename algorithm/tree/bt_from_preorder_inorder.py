"""leet code 105, medium, tags: array, hash table, divide and conquer, tree, binary tree."""
from typing import List, Optional

from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    """Recursive DFS with HashMap. O(n) time, O(n) space."""

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_idx = {v: i for i, v in enumerate(inorder)}  # O(n) space
        self.pre_id = 0

        def dfs(lo: int, hi: int) -> Optional[TreeNode]:  # O(n) time, each node visited once
            if lo > hi:
                return None
            root_val = preorder[self.pre_id]
            self.pre_id += 1
            node = TreeNode(root_val)
            mid = val_idx[root_val]
            node.left = dfs(lo, mid - 1)
            node.right = dfs(mid + 1, hi)
            return node

        return dfs(0, len(inorder) - 1)


class Solution2:
    """Iterative with stack. O(n) time, O(n) space."""

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]  # O(n) space
        in_idx = 0
        for i in range(1, len(preorder)):  # O(n) time, each node pushed/popped once
            val = preorder[i]
            node = TreeNode(val)
            if stack[-1].val != inorder[in_idx]:
                stack[-1].left = node
            else:
                parent = None
                while stack and stack[-1].val == inorder[in_idx]:
                    parent = stack.pop()
                    in_idx += 1
                parent.right = node
            stack.append(node)
        return root
