import unittest

from algorithm.tree.bt_right_side_view import Solution, Solution2
from algorithm.jzstruct.tree_node import TreeNode


class TestRightSideView(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        #       1
        #      / \
        #     2   3
        #      \   \
        #       5   4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rightSideView(root), [1, 3, 4])

    def test_example2(self):
        #     1
        #      \
        #       3
        root = TreeNode(1)
        root.right = TreeNode(3)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rightSideView(root), [1, 3])

    def test_empty(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rightSideView(None), [])

    def test_single_node(self):
        root = TreeNode(42)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rightSideView(root), [42])

    def test_left_heavy(self):
        #       1
        #      /
        #     2
        #    /
        #   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rightSideView(root), [1, 2, 3])

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
                self.assertEqual(sol.rightSideView(root), [1, 3, 7])

    def test_left_deeper(self):
        #       1
        #      / \
        #     2   3
        #    /
        #   4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rightSideView(root), [1, 3, 4])
