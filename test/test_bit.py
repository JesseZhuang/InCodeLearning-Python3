import unittest

from algorithm.tree.binary_indexed_tree import BITtree


class TestBitTree(unittest.TestCase):
    def setUp(self):
        self.tbt = BITtree([2, 1, 1, 2, 5])

    def test_get_sum(self):
        self.assertEqual(2, self.tbt.getSum(0))
        self.assertEqual(3, self.tbt.getSum(1))
        self.assertEqual(11, self.tbt.getSum(4))

    def test_update(self):
        self.tbt.update(3, 4)
        self.assertEqual(10, self.tbt.getSum(3))
        self.assertEqual(15, self.tbt.getSum(4))

    def test_rsq(self):
        self.assertEqual(3, self.tbt.rsq(0, 1))
        self.assertEqual(4, self.tbt.rsq(1, 3))
