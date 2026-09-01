"""test LeetCode 120 Triangle"""
import unittest

from algorithm.dp.triangle import Solution, Solution2


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def _make(self, triangle):
        """Deep copy to protect from in-place mutation."""
        return [row[:] for row in triangle]

    def test_example1(self):
        t = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        for sol in self.solutions:
            self.assertEqual(11, sol.minimumTotal(self._make(t)))

    def test_example2(self):
        t = [[-10]]
        for sol in self.solutions:
            self.assertEqual(-10, sol.minimumTotal(self._make(t)))

    def test_two_rows(self):
        t = [[1], [2, 3]]
        for sol in self.solutions:
            self.assertEqual(3, sol.minimumTotal(self._make(t)))

    def test_negative_values(self):
        t = [[-1], [2, 3], [1, -1, -3]]
        for sol in self.solutions:
            self.assertEqual(-1, sol.minimumTotal(self._make(t)))

    def test_all_zeros(self):
        t = [[0], [0, 0], [0, 0, 0]]
        for sol in self.solutions:
            self.assertEqual(0, sol.minimumTotal(self._make(t)))

    def test_large_values(self):
        t = [[100], [-200, 300], [400, -500, 600]]
        for sol in self.solutions:
            self.assertEqual(-600, sol.minimumTotal(self._make(t)))

    def test_greedy_fails(self):
        """Greedy picks 1->2->3=6, but optimal is 1->3->1=5."""
        t = [[1], [2, 3], [4, 3, 1]]
        for sol in self.solutions:
            self.assertEqual(5, sol.minimumTotal(self._make(t)))


if __name__ == '__main__':
    unittest.main()
