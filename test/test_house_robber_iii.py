import unittest

from algorithm.tree.house_robber_iii import Solution
from algorithm.jzstruct.tree_node import TreeNode


class TestHouseRobberIII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        #     3
        #    / \
        #   2   3
        #    \   \
        #     3   1
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rob(root), 7)

    def test_example2(self):
        #       3
        #      / \
        #     4   5
        #    / \   \
        #   1   3   1
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rob(root), 9)

    def test_single_node(self):
        root = TreeNode(5)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rob(root), 5)

    def test_none(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rob(None), 0)

    def test_left_skew(self):
        #   4
        #  /
        # 1
        #  \
        #   2
        root = TreeNode(4)
        root.left = TreeNode(1)
        root.left.right = TreeNode(2)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rob(root), 6)

    def test_all_same_values(self):
        #     1
        #    / \
        #   1   1
        #  / \
        # 1   1
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.rob(root), 3)


if __name__ == "__main__":
    unittest.main()
