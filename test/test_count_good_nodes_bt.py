import unittest

from algorithm.tree.count_good_nodes_bt import Solution, Solution2
from algorithm.jzstruct.tree_node import TreeNode


class TestCountGoodNodesBT(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        #       3
        #      / \
        #     1   4
        #    /   / \
        #   3   1   5
        # Good nodes: 3 (root), 3 (left-left), 4, 5 → 4
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.left = TreeNode(3)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.goodNodes(root), 4)

    def test_example2(self):
        #     3
        #    /
        #   3
        #  / \
        # 4   2
        # Good nodes: 3 (root), 3 (left), 4 → 3
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(2)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.goodNodes(root), 3)

    def test_single_node(self):
        root = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.goodNodes(root), 1)

    def test_all_same_value(self):
        #     5
        #    / \
        #   5   5
        # All nodes are good
        root = TreeNode(5)
        root.left = TreeNode(5)
        root.right = TreeNode(5)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.goodNodes(root), 3)

    def test_decreasing_path(self):
        # 10 -> 5 -> 3 -> 1, only root is good
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.goodNodes(root), 1)

    def test_increasing_path(self):
        # 1 -> 2 -> 3 -> 4, all nodes are good
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.goodNodes(root), 4)

    def test_negative_values(self):
        #     -1
        #    /  \
        #  -2   -3
        # Good nodes: -1 (root) only. -2 < -1, -3 < -1
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.goodNodes(root), 1)

    def test_negative_with_good_children(self):
        #     -10
        #    /   \
        #  -5    -10
        # Good: -10 (root), -5 (>= -10), -10 (>= -10) → 3
        root = TreeNode(-10)
        root.left = TreeNode(-5)
        root.right = TreeNode(-10)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.goodNodes(root), 3)
