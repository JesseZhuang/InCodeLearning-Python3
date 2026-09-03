import unittest

from algorithm.tree.max_width_bt import Solution, Solution2
from algorithm.jzstruct.tree_node import TreeNode


class TestMaxWidthBT(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        #       1
        #      / \
        #     3   2
        #    / \   \
        #   5   3   9
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(9)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.widthOfBinaryTree(root), 4)

    def test_example2(self):
        #       1
        #      / \
        #     3   2
        #    /     \
        #   5       9
        #  /       /
        # 6       7
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.right.right = TreeNode(9)
        root.left.left.left = TreeNode(6)
        root.right.right.left = TreeNode(7)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.widthOfBinaryTree(root), 7)

    def test_example3(self):
        #     1
        #    / \
        #   3   2
        #  /
        # 5
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.widthOfBinaryTree(root), 2)

    def test_single_node(self):
        root = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.widthOfBinaryTree(root), 1)

    def test_left_skewed(self):
        # 1 -> 2 -> 3 (all left children)
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.widthOfBinaryTree(root), 1)

    def test_right_skewed(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.widthOfBinaryTree(root), 1)

    def test_complete_tree(self):
        #       1
        #      / \
        #     2   3
        #    / \ / \
        #   4  5 6  7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.widthOfBinaryTree(root), 4)

    def test_wide_gap(self):
        #     1
        #    / \
        #   2   3
        #  /     \
        # 4       5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.widthOfBinaryTree(root), 4)
