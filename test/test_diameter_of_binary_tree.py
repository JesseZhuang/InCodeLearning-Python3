import unittest

from algorithm.tree.diameter_of_binary_tree import Solution
from algorithm.jzstruct.tree_node import TreeNode


class TestDiameterOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.diameterOfBinaryTree(root), 3)

    def test_example2(self):
        #   1
        #  /
        # 2
        root = TreeNode(1)
        root.left = TreeNode(2)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.diameterOfBinaryTree(root), 1)

    def test_single_node(self):
        root = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.diameterOfBinaryTree(root), 0)

    def test_empty(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.diameterOfBinaryTree(None), 0)

    def test_linear_left(self):
        # 1 -> 2 -> 3 -> 4  (all left children)
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.diameterOfBinaryTree(root), 3)

    def test_diameter_not_through_root(self):
        #         1
        #        /
        #       2
        #      / \
        #     3   4
        #    /     \
        #   5       6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(5)
        root.left.right.right = TreeNode(6)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                # path: 5 -> 3 -> 2 -> 4 -> 6, length = 4
                self.assertEqual(sol.diameterOfBinaryTree(root), 4)

    def test_balanced_tree(self):
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
                # path: 4->2->1->3->7 or similar, length = 4
                self.assertEqual(sol.diameterOfBinaryTree(root), 4)
