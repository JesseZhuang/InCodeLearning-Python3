import unittest

from algorithm.tree.amount_of_time_infected import Solution, Solution2
from algorithm.jzstruct.tree_node import TreeNode


class TestAmountOfTimeInfected(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        #         1
        #        / \
        #       5   3
        #      /   / \
        #     4   10   6
        #    / \
        #   9   2
        # start = 3, answer = 4 (3->10 is 1, 3->6 is 1, 3->1->5->4->9 is 4)
        root = TreeNode(1)
        root.left = TreeNode(5)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(6)
        root.left.left.left = TreeNode(9)
        root.left.left.right = TreeNode(2)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.amountOfTime(root, 3), 4)

    def test_example2(self):
        # Single node
        root = TreeNode(1)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.amountOfTime(root, 1), 0)

    def test_start_at_root(self):
        #     1
        #    / \
        #   2   3
        #  /
        # 4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.amountOfTime(root, 1), 2)

    def test_start_at_leaf(self):
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        # start = 4, answer = 3 (4->2->1->3)
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.amountOfTime(root, 4), 3)

    def test_linear_tree(self):
        # 1 -> 2 -> 3 -> 4 (all left children), start = 2
        # answer = 2 (2->1 is 1, 2->3->4 is 2)
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.amountOfTime(root, 2), 2)

    def test_deep_right_branch(self):
        #       1
        #      / \
        #     2   3
        #          \
        #           4
        #            \
        #             5
        # start = 1, answer = 3 (1->3->4->5)
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(5)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.amountOfTime(root, 1), 3)
