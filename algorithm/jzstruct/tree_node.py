"""Definition for a binary tree node."""


class TreeNode:
    """BT"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ParentTreeNode:
    """BT with a link to the parent"""

    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
