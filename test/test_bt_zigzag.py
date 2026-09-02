import unittest

from algorithm.tree.bt_zigzag import Solution1, Solution2, Solution3
from algorithm.jzstruct.tree_node import TreeNode


class TestBTZigzag(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution1(), Solution2(), Solution3()]

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
        expected = [[3], [20, 9], [15, 7]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.zigzagLevelOrder(root), expected)

    def test_single_node(self):
        root = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.zigzagLevelOrder(root), [[1]])

    def test_empty(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.zigzagLevelOrder(None), [])

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
        expected = [[1], [3, 2], [4, 5, 6, 7]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.zigzagLevelOrder(root), expected)

    def test_left_skewed(self):
        #   1
        #  /
        # 2
        #  \
        #   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        expected = [[1], [2], [3]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.zigzagLevelOrder(root), expected)

    def test_right_skewed(self):
        # 1
        #  \
        #   2
        #    \
        #     3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        expected = [[1], [2], [3]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.zigzagLevelOrder(root), expected)

    def test_four_levels(self):
        #         1
        #        / \
        #       2   3
        #      /     \
        #     4       5
        #    /         \
        #   6           7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.left.left.left = TreeNode(6)
        root.right.right.right = TreeNode(7)
        expected = [[1], [3, 2], [4, 5], [7, 6]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.zigzagLevelOrder(root), expected)

    def test_negative_values(self):
        root = TreeNode(-100)
        root.left = TreeNode(0)
        root.right = TreeNode(100)
        expected = [[-100], [100, 0]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.zigzagLevelOrder(root), expected)
