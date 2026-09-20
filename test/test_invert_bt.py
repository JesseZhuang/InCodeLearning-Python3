import unittest

from algorithm.tree.invert_bt import Solution, Solution2
from algorithm.jzstruct.tree_node import TreeNode


def tree_to_list(root):
    """Level-order traversal to list for easy comparison."""
    if not root: return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def build_tree(vals):
    """Build tree from level-order list."""
    if not vals: return None
    root = TreeNode(vals[0])
    queue, i = [root], 1
    while queue and i < len(vals):
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


class TestInvertBT(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            root = build_tree([4, 2, 7, 1, 3, 6, 9])
            result = sol.invertTree(root)
            self.assertEqual(tree_to_list(result), [4, 7, 2, 9, 6, 3, 1])

    def test_example2(self):
        for sol in self.solutions:
            root = build_tree([2, 1, 3])
            result = sol.invertTree(root)
            self.assertEqual(tree_to_list(result), [2, 3, 1])

    def test_empty(self):
        for sol in self.solutions:
            self.assertIsNone(sol.invertTree(None))

    def test_single_node(self):
        for sol in self.solutions:
            root = TreeNode(1)
            result = sol.invertTree(root)
            self.assertEqual(tree_to_list(result), [1])

    def test_left_only(self):
        for sol in self.solutions:
            root = build_tree([1, 2, None, 3])
            result = sol.invertTree(root)
            self.assertEqual(tree_to_list(result), [1, None, 2, None, 3])

    def test_right_only(self):
        for sol in self.solutions:
            root = build_tree([1, None, 2, None, 3])
            result = sol.invertTree(root)
            self.assertEqual(tree_to_list(result), [1, 2, None, 3])

    def test_double_invert_restores(self):
        for sol in self.solutions:
            original = [4, 2, 7, 1, 3, 6, 9]
            root = build_tree(original)
            root = sol.invertTree(root)
            root = sol.invertTree(root)
            self.assertEqual(tree_to_list(root), original)

    def test_asymmetric(self):
        #       1
        #      / \
        #     2   3
        #    /
        #   4
        for sol in self.solutions:
            root = build_tree([1, 2, 3, 4])
            result = sol.invertTree(root)
            self.assertEqual(tree_to_list(result), [1, 3, 2, None, None, None, 4])
