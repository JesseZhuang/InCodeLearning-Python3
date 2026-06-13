import unittest

from algorithm.jzstruct.tree_node import TreeNode
from algorithm.tree.validate_bst import Solution, Solution2


class TestValidateBST(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_valid_bst(self):
        """[2,1,3] -> True"""
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        for sol in self.solutions:
            self.assertTrue(sol.isValidBST(root))

    def test_invalid_bst(self):
        """[5,1,4,null,null,3,6] -> False (4 < 5 but in right subtree)"""
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4, TreeNode(3), TreeNode(6))
        for sol in self.solutions:
            self.assertFalse(sol.isValidBST(root))

    def test_single_node(self):
        root = TreeNode(1)
        for sol in self.solutions:
            self.assertTrue(sol.isValidBST(root))

    def test_equal_values(self):
        """[2,2,2] -> False (BST requires strict inequality)"""
        root = TreeNode(2, TreeNode(2), TreeNode(2))
        for sol in self.solutions:
            self.assertFalse(sol.isValidBST(root))

    def test_left_subtree_violation(self):
        """[5,4,6,null,null,3,7] -> False (3 in right subtree but < 5)"""
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(6, TreeNode(3), TreeNode(7))
        for sol in self.solutions:
            self.assertFalse(sol.isValidBST(root))

    def test_large_values(self):
        """[2147483647] -> True (max int32)"""
        root = TreeNode(2147483647)
        for sol in self.solutions:
            self.assertTrue(sol.isValidBST(root))

    def test_skewed_left(self):
        """3->2->1 all left -> True"""
        root = TreeNode(3, TreeNode(2, TreeNode(1), None), None)
        for sol in self.solutions:
            self.assertTrue(sol.isValidBST(root))

    def test_skewed_right(self):
        """1->2->3 all right -> True"""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        for sol in self.solutions:
            self.assertTrue(sol.isValidBST(root))


if __name__ == '__main__':
    unittest.main()
