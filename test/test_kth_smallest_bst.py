from unittest import TestCase

from algorithm.jzstruct.tree_node import TreeNode
from algorithm.tree.kth_smallest_bst import Solution


class TestKthSmallestBST(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        """tree [3,1,4,null,2], k=1 -> 1"""
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        for sol in self.solutions:
            self.assertEqual(1, sol.kthSmallest(root, 1))

    def test_example2(self):
        """tree [5,3,6,2,4,null,null,1], k=3 -> 3"""
        root = TreeNode(5,
                        TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
                        TreeNode(6))
        for sol in self.solutions:
            self.assertEqual(3, sol.kthSmallest(root, 3))

    def test_single_node(self):
        """single node, k=1"""
        root = TreeNode(42)
        for sol in self.solutions:
            self.assertEqual(42, sol.kthSmallest(root, 1))

    def test_right_skewed(self):
        """right-skewed tree [1,null,2,null,3], k=2 -> 2"""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        for sol in self.solutions:
            self.assertEqual(2, sol.kthSmallest(root, 2))

    def test_left_skewed(self):
        """left-skewed tree [3,2,null,1], k=3 -> 3"""
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        for sol in self.solutions:
            self.assertEqual(3, sol.kthSmallest(root, 3))

    def test_k_equals_n(self):
        """k equals total number of nodes (largest element)"""
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        for sol in self.solutions:
            self.assertEqual(3, sol.kthSmallest(root, 3))
