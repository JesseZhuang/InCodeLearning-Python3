from unittest import TestCase

from algorithm.tree.bt_from_io_po import Solution


class TestSolution(TestCase):
    def test_build_tree(self):
        """self.root_id not defined in __init__, still ok"""
        tbt = Solution()
        root = tbt.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
        self.assertEqual(3, root.val)
        self.assertEqual(9, root.left.val)
        self.assertEqual(20, root.right.val)
