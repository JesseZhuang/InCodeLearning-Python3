"""leet 889, medium"""
from typing import Optional

from jzstruct.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.pre_index = 0
        self.post_index = 0

    # Helper function to recursively build the tree
    def constructFromPrePost(
            self, preorder: list[int], postorder: list[int]
    ) -> Optional[TreeNode]:
        return self._construct_tree(preorder, postorder)

    def _construct_tree(
            self, preorder: list[int], postorder: list[int]
    ) -> Optional[TreeNode]:
        root = TreeNode(preorder[self.pre_index])
        self.pre_index += 1

        # Recursively construct the left subtree if the root is not the last of
        # its subtree
        if root.val != postorder[self.post_index]:
            root.left = self._construct_tree(preorder, postorder)

        # Recursively construct the right subtree if the root is not the last of
        # its subtree
        if root.val != postorder[self.post_index]:
            root.right = self._construct_tree(preorder, postorder)

        # Mark this node and its subtree as fully processed
        self.post_index += 1
        return root
