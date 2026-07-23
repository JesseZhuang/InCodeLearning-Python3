import unittest

from algorithm.tree.path_sum_iii import Solution, Solution2, TreeNode


class TestPathSumIII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def build_tree(self, vals):
        """Build tree from level-order list (None for missing nodes)."""
        if not vals:
            return None
        root = TreeNode(vals[0])
        queue = [root]
        i = 1
        while i < len(vals):
            node = queue.pop(0)
            if i < len(vals) and vals[i] is not None:
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1
        return root

    def test_example1(self):
        # [10,5,-3,3,2,null,11,3,-2,null,1], targetSum=8
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(-3)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)
        root.right.right = TreeNode(11)
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right.right = TreeNode(1)
        for sol in self.solutions:
            self.assertEqual(sol.pathSum(root, 8), 3, f"Failed for {sol.__class__.__name__}")

    def test_example2(self):
        # [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum=22
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        for sol in self.solutions:
            self.assertEqual(sol.pathSum(root, 22), 3, f"Failed for {sol.__class__.__name__}")

    def test_empty_tree(self):
        for sol in self.solutions:
            self.assertEqual(sol.pathSum(None, 0), 0)

    def test_single_node_match(self):
        root = TreeNode(5)
        for sol in self.solutions:
            self.assertEqual(sol.pathSum(root, 5), 1)

    def test_single_node_no_match(self):
        root = TreeNode(5)
        for sol in self.solutions:
            self.assertEqual(sol.pathSum(root, 3), 0)

    def test_negative_values(self):
        # -2 -> -3, target -5 (one path: -2 -> -3)
        root = TreeNode(-2)
        root.right = TreeNode(-3)
        for sol in self.solutions:
            self.assertEqual(sol.pathSum(root, -5), 1)

    def test_multiple_paths_same_sum(self):
        # 1 -> 1 -> 1, target 2: paths are [1,1](top two), [1,1](bottom two)
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.left.left = TreeNode(1)
        for sol in self.solutions:
            self.assertEqual(sol.pathSum(root, 2), 2)

    def test_zero_target(self):
        # 0 -> 0 -> 0, target 0: every subpath sums to 0
        root = TreeNode(0)
        root.left = TreeNode(0)
        root.left.left = TreeNode(0)
        for sol in self.solutions:
            # paths: [0], [0], [0], [0,0], [0,0], [0,0,0] = 6
            self.assertEqual(sol.pathSum(root, 0), 6)

    def test_large_values(self):
        root = TreeNode(1000000000)
        root.left = TreeNode(1000000000)
        root.left.left = TreeNode(1000000000)
        for sol in self.solutions:
            self.assertEqual(sol.pathSum(root, 1000000000), 3)


if __name__ == '__main__':
    unittest.main()
