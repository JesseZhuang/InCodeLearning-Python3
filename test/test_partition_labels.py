import unittest

from algorithm.jzarray.partition_labels import Solution, Solution2


class TestPartitionLabels(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual([9, 7, 8], sol.partitionLabels("ababcbacadefegdehijhklij"))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual([10], sol.partitionLabels("eccbbbbdec"))

    def test_single_char(self):
        for sol in self.solutions:
            self.assertEqual([1], sol.partitionLabels("a"))

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual([5], sol.partitionLabels("aaaaa"))

    def test_all_unique(self):
        for sol in self.solutions:
            self.assertEqual([1, 1, 1, 1], sol.partitionLabels("abcd"))

    def test_two_partitions(self):
        for sol in self.solutions:
            self.assertEqual([2, 2], sol.partitionLabels("aabb"))

    def test_last_char_extends(self):
        for sol in self.solutions:
            self.assertEqual([5, 1], sol.partitionLabels("abcba" + "d"))

    def test_long_single_partition(self):
        for sol in self.solutions:
            self.assertEqual([27], sol.partitionLabels("abcdefghijklmnopqrstuvwxyza"))


if __name__ == "__main__":
    unittest.main()
