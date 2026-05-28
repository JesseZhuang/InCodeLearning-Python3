from unittest import TestCase

from algorithm.jzstruct.tree_node import TreeNode
from algorithm.tree.max_path_sum import Solution


class TestMaxPathSum(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        #   1
        #  / \
        # 2   3
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        for sol in self.solutions:
            self.assertEqual(6, sol.maxPathSum(root))

    def test_example2(self):
        #    -10
        #    / \
        #   9  20
        #     /  \
        #    15   7
        root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        for sol in self.solutions:
            self.assertEqual(42, sol.maxPathSum(root))

    def test_single_node(self):
        root = TreeNode(1)
        for sol in self.solutions:
            self.assertEqual(1, sol.maxPathSum(root))

    def test_single_negative(self):
        root = TreeNode(-3)
        for sol in self.solutions:
            self.assertEqual(-3, sol.maxPathSum(root))

    def test_all_negative(self):
        #    -1
        #    / \
        #  -2  -3
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        for sol in self.solutions:
            self.assertEqual(-1, sol.maxPathSum(root))

    def test_path_not_through_root(self):
        #       1
        #      /
        #     2
        #    / \
        #   3   4
        root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)))
        for sol in self.solutions:
            self.assertEqual(9, sol.maxPathSum(root))

    def test_left_skewed(self):
        #   -2
        #   /
        #  1
        root = TreeNode(-2, TreeNode(1))
        for sol in self.solutions:
            self.assertEqual(1, sol.maxPathSum(root))

    def test_max_constraint_values(self):
        # Node values at boundary: -1000, 1000
        root = TreeNode(1000, TreeNode(-1000), TreeNode(1000))
        for sol in self.solutions:
            self.assertEqual(2000, sol.maxPathSum(root))
