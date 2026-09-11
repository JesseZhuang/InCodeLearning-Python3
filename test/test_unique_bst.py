"""test LeetCode 96 Unique Binary Search Trees"""
import unittest

from algorithm.dp.unique_bst import Solution, Solution2


class TestUniqueBST(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.numTrees(3))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.numTrees(1))

    def test_n_zero(self):
        """0 nodes -> 1 empty tree."""
        for sol in self.solutions:
            self.assertEqual(1, sol.numTrees(0))

    def test_n_two(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.numTrees(2))

    def test_n_four(self):
        for sol in self.solutions:
            self.assertEqual(14, sol.numTrees(4))

    def test_n_five(self):
        for sol in self.solutions:
            self.assertEqual(42, sol.numTrees(5))

    def test_upper_bound(self):
        """Constraint: 1 <= n <= 19."""
        for sol in self.solutions:
            self.assertEqual(1767263190, sol.numTrees(19))


if __name__ == '__main__':
    unittest.main()
