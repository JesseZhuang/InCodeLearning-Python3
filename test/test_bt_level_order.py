import unittest

from algorithm.tree.bt_level_order import Solution, Solution2
from algorithm.jzstruct.tree_node import TreeNode


class TestLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        #       3
        #      / \
        #     9  20
        #        / \
        #       15  7
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.levelOrder(root), [[3], [9, 20], [15, 7]])

    def test_single_node(self):
        root = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.levelOrder(root), [[1]])

    def test_empty(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.levelOrder(None), [])

    def test_left_skewed(self):
        #   1
        #  /
        # 2
        #  \
        #   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.levelOrder(root), [[1], [2], [3]])

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
                self.assertEqual(sol.levelOrder(root), [[1], [2, 3], [4, 5, 6, 7]])

    def test_negative_values(self):
        root = TreeNode(-10)
        root.left = TreeNode(-20)
        root.right = TreeNode(-30)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.levelOrder(root), [[-10], [-20, -30]])
