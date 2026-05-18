from unittest import TestCase

from algorithm.jzstruct.tree_node import TreeNode
from algorithm.tree.kth_largest_sum_bt import Solution, Solution2


class TestKthLargestSumBT(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        #       5
        #      / \
        #     8   9
        #    / \ / \
        #   2  1 3  7
        #  /
        # 4
        root = TreeNode(5,
                        TreeNode(8, TreeNode(2, TreeNode(4)), TreeNode(1)),
                        TreeNode(9, TreeNode(3), TreeNode(7)))
        for sol in self.solutions:
            self.assertEqual(13, sol.kthLargestLevelSum(root, 2))

    def test_example2(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        for sol in self.solutions:
            self.assertEqual(3, sol.kthLargestLevelSum(root, 1))

    def test_k_exceeds_depth(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        for sol in self.solutions:
            self.assertEqual(-1, sol.kthLargestLevelSum(root, 3))

    def test_single_node(self):
        root = TreeNode(42)
        for sol in self.solutions:
            self.assertEqual(42, sol.kthLargestLevelSum(root, 1))

    def test_null_root(self):
        for sol in self.solutions:
            self.assertEqual(-1, sol.kthLargestLevelSum(None, 1))

    def test_negative_values(self):
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        for sol in self.solutions:
            self.assertEqual(-1, sol.kthLargestLevelSum(root, 1))
            self.assertEqual(-5, sol.kthLargestLevelSum(root, 2))

    def test_k_equals_depth(self):
        #     1
        #    / \
        #   2   3
        #  /
        # 4
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        for sol in self.solutions:
            self.assertEqual(1, sol.kthLargestLevelSum(root, 3))
