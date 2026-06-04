import unittest

from algorithm.tree.flatten_bt_to_linked_list import Solution, Solution2
from algorithm.jzstruct.tree_node import TreeNode


def tree_to_list(root):
    """Convert flattened tree (right-only linked list) to a list of values."""
    res = []
    while root:
        res.append(root.val)
        root = root.right
    return res


class TestFlatten(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def _build_example1(self):
        #       1
        #      / \
        #     2   5
        #    / \   \
        #   3   4   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        return root

    def test_example1(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                root = self._build_example1()
                sol.flatten(root)
                self.assertEqual(tree_to_list(root), [1, 2, 3, 4, 5, 6])

    def test_single_node(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                root = TreeNode(0)
                sol.flatten(root)
                self.assertEqual(tree_to_list(root), [0])

    def test_empty(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                sol.flatten(None)

    def test_left_only(self):
        #     1
        #    /
        #   2
        #  /
        # 3
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                root = TreeNode(1)
                root.left = TreeNode(2)
                root.left.left = TreeNode(3)
                sol.flatten(root)
                self.assertEqual(tree_to_list(root), [1, 2, 3])

    def test_right_only(self):
        # 1 -> 2 -> 3 already flat
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                root = TreeNode(1)
                root.right = TreeNode(2)
                root.right.right = TreeNode(3)
                sol.flatten(root)
                self.assertEqual(tree_to_list(root), [1, 2, 3])

    def test_all_left_null(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                root = self._build_example1()
                sol.flatten(root)
                cur = root
                while cur:
                    self.assertIsNone(cur.left)
                    cur = cur.right
