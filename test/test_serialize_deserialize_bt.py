import unittest

from algorithm.tree.serialize_deserialize_bt import Codec, Codec2
from algorithm.jzstruct.tree_node import TreeNode


def trees_equal(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and trees_equal(a.left, b.left) and trees_equal(a.right, b.right)


class TestSerializeDeserializeBT(unittest.TestCase):
    def setUp(self):
        self.codecs = [Codec(), Codec2()]

    def test_example1(self):
        #       1
        #      / \
        #     2   3
        #        / \
        #       4   5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        for codec in self.codecs:
            with self.subTest(codec=codec.__class__.__name__):
                data = codec.serialize(root)
                result = codec.deserialize(data)
                self.assertTrue(trees_equal(root, result))

    def test_empty_tree(self):
        for codec in self.codecs:
            with self.subTest(codec=codec.__class__.__name__):
                data = codec.serialize(None)
                result = codec.deserialize(data)
                self.assertIsNone(result)

    def test_single_node(self):
        root = TreeNode(42)
        for codec in self.codecs:
            with self.subTest(codec=codec.__class__.__name__):
                data = codec.serialize(root)
                result = codec.deserialize(data)
                self.assertTrue(trees_equal(root, result))

    def test_left_skewed(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        for codec in self.codecs:
            with self.subTest(codec=codec.__class__.__name__):
                data = codec.serialize(root)
                result = codec.deserialize(data)
                self.assertTrue(trees_equal(root, result))

    def test_right_skewed(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        for codec in self.codecs:
            with self.subTest(codec=codec.__class__.__name__):
                data = codec.serialize(root)
                result = codec.deserialize(data)
                self.assertTrue(trees_equal(root, result))

    def test_negative_values(self):
        root = TreeNode(-1)
        root.left = TreeNode(-1000)
        root.right = TreeNode(1000)
        for codec in self.codecs:
            with self.subTest(codec=codec.__class__.__name__):
                data = codec.serialize(root)
                result = codec.deserialize(data)
                self.assertTrue(trees_equal(root, result))

    def test_large_tree(self):
        # Complete binary tree of depth 3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        for codec in self.codecs:
            with self.subTest(codec=codec.__class__.__name__):
                data = codec.serialize(root)
                result = codec.deserialize(data)
                self.assertTrue(trees_equal(root, result))


if __name__ == '__main__':
    unittest.main()
