import unittest

from algorithm.tree.all_nodes_distance_k_bt import Solution, Solution2
from algorithm.jzstruct.tree_node import TreeNode


class TestAllNodesDistanceK(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        #         3
        #        / \
        #       5   1
        #      / \ / \
        #     6  2 0  8
        #       / \
        #      7   4
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        target = root.left  # node 5
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.distanceK(root, target, 2)
                self.assertEqual(sorted(result), [1, 4, 7])

    def test_k_zero(self):
        root = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.distanceK(root, root, 0), [1])

    def test_single_node_k_nonzero(self):
        root = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.distanceK(root, root, 1), [])

    def test_target_is_root(self):
        #     1
        #    / \
        #   2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.distanceK(root, root, 1)
                self.assertEqual(sorted(result), [2, 3])

    def test_target_is_leaf(self):
        #       1
        #      /
        #     2
        #    /
        #   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        target = root.left.left  # node 3
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.distanceK(root, target, 2)
                self.assertEqual(result, [1])

    def test_k_greater_than_tree_height(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.distanceK(root, root, 5), [])

    def test_all_nodes_at_distance(self):
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
        target = root.left  # node 2
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.distanceK(root, target, 1)
                self.assertEqual(sorted(result), [1, 4, 5])
