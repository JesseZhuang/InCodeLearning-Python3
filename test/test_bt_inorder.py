import unittest

from algorithm.jzstruct.tree_node import TreeNode
from algorithm.tree.bt_inorder import Solution, Solution2


class TestBinaryTreeInorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_empty_tree(self):
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(solution.inorderTraversal(None), [])

    def test_single_node(self):
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(solution.inorderTraversal(TreeNode(1)), [1])

    def test_balanced_tree(self):
        #       4
        #      / \
        #     2   6
        #    / \ / \
        #   1  3 5  7
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(solution.inorderTraversal(root), [1, 2, 3, 4, 5, 6, 7])

    def test_right_child_with_left_descendant(self):
        # 1
        #  \
        #   2
        #  /
        # 3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(solution.inorderTraversal(root), [1, 3, 2])
