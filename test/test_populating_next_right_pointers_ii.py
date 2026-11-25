import unittest

from algorithm.tree.populating_next_right_pointers_ii import Node, Solution


class TestPopulatingNextRightPointersII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution().connect, Solution().connectConstantSpace]

    def test_empty_tree_returns_none(self):
        for connect in self.solutions:
            with self.subTest(connect=connect.__name__):
                self.assertIsNone(connect(None))

    def test_single_node_keeps_next_none(self):
        for connect in self.solutions:
            with self.subTest(connect=connect.__name__):
                root = Node(1)
                self.assertIs(connect(root), root)
                self.assertIsNone(root.next)

    def test_sparse_levels_link_across_parents(self):
        for connect in self.solutions:
            with self.subTest(connect=connect.__name__):
                root = Node(1)
                root.left = Node(2)
                root.right = Node(3)
                root.left.left = Node(4)
                root.left.right = Node(5)
                root.right.right = Node(7)

                self.assertIs(connect(root), root)
                self.assertIsNone(root.next)
                self.assertIs(root.left.next, root.right)
                self.assertIsNone(root.right.next)
                self.assertIs(root.left.left.next, root.left.right)
                self.assertIs(root.left.right.next, root.right.right)
                self.assertIsNone(root.right.right.next)

    def test_maximum_depth_chain_is_handled_iteratively(self):
        for connect in self.solutions:
            with self.subTest(connect=connect.__name__):
                root = Node(0)
                current = root
                for value in range(1, 6000):
                    current.left = Node(value)
                    current = current.left

                self.assertIs(connect(root), root)
                current = root
                while current is not None:
                    self.assertIsNone(current.next)
                    current = current.left

    def test_one_sided_tree_keeps_each_level_tail_none(self):
        for connect in self.solutions:
            with self.subTest(connect=connect.__name__):
                root = Node(1)
                root.left = Node(2)
                root.left.right = Node(3)
                root.left.right.left = Node(4)

                self.assertIs(connect(root), root)
                self.assertIsNone(root.next)
                self.assertIsNone(root.left.next)
                self.assertIsNone(root.left.right.next)
                self.assertIsNone(root.left.right.left.next)


if __name__ == "__main__":
    unittest.main()
