import unittest

from algorithm.tree.subtree_of_another_tree import Solution, Solution2
from algorithm.jzstruct.tree_node import TreeNode


class TestSubtreeOfAnotherTree(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        #     3
        #    / \
        #   4   5
        #  / \
        # 1   2
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        sub = TreeNode(4)
        sub.left = TreeNode(1)
        sub.right = TreeNode(2)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.isSubtree(root, sub))

    def test_example2(self):
        #       3
        #      / \
        #     4   5
        #    / \
        #   1   2
        #      /
        #     0
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(0)
        sub = TreeNode(4)
        sub.left = TreeNode(1)
        sub.right = TreeNode(2)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertFalse(sol.isSubtree(root, sub))

    def test_single_node_match(self):
        root = TreeNode(1)
        sub = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.isSubtree(root, sub))

    def test_single_node_no_match(self):
        root = TreeNode(1)
        sub = TreeNode(2)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertFalse(sol.isSubtree(root, sub))

    def test_root_is_subtree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        sub = TreeNode(1)
        sub.left = TreeNode(2)
        sub.right = TreeNode(3)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.isSubtree(root, sub))

    def test_null_root(self):
        sub = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertFalse(sol.isSubtree(None, sub))

    def test_value_prefix_trap(self):
        # [12] should not match [2] — boundary markers prevent false match
        root = TreeNode(12)
        sub = TreeNode(2)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertFalse(sol.isSubtree(root, sub))

    def test_negative_values(self):
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        sub = TreeNode(-2)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.isSubtree(root, sub))

    def test_deep_right(self):
        # root: 1 -> right 2 -> right 3
        # sub: 2 -> right 3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        sub = TreeNode(2)
        sub.right = TreeNode(3)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.isSubtree(root, sub))
