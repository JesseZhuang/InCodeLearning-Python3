from unittest import TestCase

from algorithm.tree.bt_from_preorder_inorder import Solution, Solution2


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, preorder, inorder, expected_root_val, check_fn):
        for sol in self.solutions:
            root = sol.buildTree(preorder, inorder)
            self.assertEqual(expected_root_val, root.val)
            check_fn(root)

    def test_example1(self):
        # [3,9,20,null,null,15,7]
        for sol in self.solutions:
            root = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
            self.assertEqual(3, root.val)
            self.assertEqual(9, root.left.val)
            self.assertEqual(20, root.right.val)
            self.assertIsNone(root.left.left)
            self.assertIsNone(root.left.right)
            self.assertEqual(15, root.right.left.val)
            self.assertEqual(7, root.right.right.val)

    def test_example2(self):
        for sol in self.solutions:
            root = sol.buildTree([-1], [-1])
            self.assertEqual(-1, root.val)
            self.assertIsNone(root.left)
            self.assertIsNone(root.right)

    def test_left_skewed(self):
        for sol in self.solutions:
            root = sol.buildTree([1, 2, 3], [3, 2, 1])
            self.assertEqual(1, root.val)
            self.assertEqual(2, root.left.val)
            self.assertEqual(3, root.left.left.val)
            self.assertIsNone(root.right)

    def test_right_skewed(self):
        for sol in self.solutions:
            root = sol.buildTree([1, 2, 3], [1, 2, 3])
            self.assertEqual(1, root.val)
            self.assertIsNone(root.left)
            self.assertEqual(2, root.right.val)
            self.assertIsNone(root.right.left)
            self.assertEqual(3, root.right.right.val)

    def test_empty(self):
        for sol in self.solutions:
            root = sol.buildTree([], [])
            self.assertIsNone(root)

    def test_two_nodes_left(self):
        for sol in self.solutions:
            root = sol.buildTree([1, 2], [2, 1])
            self.assertEqual(1, root.val)
            self.assertEqual(2, root.left.val)
            self.assertIsNone(root.right)

    def test_two_nodes_right(self):
        for sol in self.solutions:
            root = sol.buildTree([1, 2], [1, 2])
            self.assertEqual(1, root.val)
            self.assertIsNone(root.left)
            self.assertEqual(2, root.right.val)

    def test_negative_values(self):
        for sol in self.solutions:
            root = sol.buildTree([-10, -20, -30], [-20, -10, -30])
            self.assertEqual(-10, root.val)
            self.assertEqual(-20, root.left.val)
            self.assertEqual(-30, root.right.val)
