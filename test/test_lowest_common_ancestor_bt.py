import unittest

from algorithm.jzstruct.tree_node import TreeNode
from algorithm.tree.lowest_common_ancestor_bt import Solution, Solution2


class TestLowestCommonAncestorBT(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def build_tree(self):
        """Build tree: [3,5,1,6,2,0,8,null,null,7,4]"""
        self.n3 = TreeNode(3)
        self.n5 = TreeNode(5)
        self.n1 = TreeNode(1)
        self.n6 = TreeNode(6)
        self.n2 = TreeNode(2)
        self.n0 = TreeNode(0)
        self.n8 = TreeNode(8)
        self.n7 = TreeNode(7)
        self.n4 = TreeNode(4)
        self.n3.left, self.n3.right = self.n5, self.n1
        self.n5.left, self.n5.right = self.n6, self.n2
        self.n1.left, self.n1.right = self.n0, self.n8
        self.n2.left, self.n2.right = self.n7, self.n4

    def test_lca_different_subtrees(self):
        """p=5, q=1, LCA should be 3 (root)."""
        self.build_tree()
        for sol in self.solutions:
            self.assertEqual(sol.lowestCommonAncestor(self.n3, self.n5, self.n1), self.n3)

    def test_lca_ancestor_is_one_node(self):
        """p=5, q=4, LCA should be 5 (p is ancestor of q)."""
        self.build_tree()
        for sol in self.solutions:
            self.assertEqual(sol.lowestCommonAncestor(self.n3, self.n5, self.n4), self.n5)

    def test_lca_two_node_tree(self):
        """root=[1,2], p=1, q=2, LCA should be 1."""
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n1.left = n2
        for sol in self.solutions:
            self.assertEqual(sol.lowestCommonAncestor(n1, n1, n2), n1)

    def test_lca_deep_nodes_same_subtree(self):
        """p=7, q=4, LCA should be 2."""
        self.build_tree()
        for sol in self.solutions:
            self.assertEqual(sol.lowestCommonAncestor(self.n3, self.n7, self.n4), self.n2)

    def test_lca_leaf_and_internal(self):
        """p=6, q=4, LCA should be 5."""
        self.build_tree()
        for sol in self.solutions:
            self.assertEqual(sol.lowestCommonAncestor(self.n3, self.n6, self.n4), self.n5)


if __name__ == '__main__':
    unittest.main()
