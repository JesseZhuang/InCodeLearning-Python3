import unittest

from algorithm.stack.next_greater_element_ii import Solution, Solution2


class TestNextGreaterElementII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(
                [2, 3, 4, -1, 4],
                sol.nextGreaterElements([1, 2, 3, 4, 3]),
            )

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(
                [2, -1, 2],
                sol.nextGreaterElements([1, 2, 1]),
            )

    def test_single(self):
        for sol in self.solutions:
            self.assertEqual([-1], sol.nextGreaterElements([5]))

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(
                [-1, -1, -1],
                sol.nextGreaterElements([3, 3, 3]),
            )

    def test_decreasing(self):
        for sol in self.solutions:
            self.assertEqual(
                [5, 5, -1],
                sol.nextGreaterElements([4, 3, 5]),
            )

    def test_increasing(self):
        for sol in self.solutions:
            self.assertEqual(
                [2, 3, 4, -1],
                sol.nextGreaterElements([1, 2, 3, 4]),
            )

    def test_circular_wrap(self):
        """The next greater for the max element wraps but finds nothing."""
        for sol in self.solutions:
            self.assertEqual(
                [5, 5, -1, 4, 5],
                sol.nextGreaterElements([3, 1, 5, 2, 4]),
            )

    def test_two_elements(self):
        for sol in self.solutions:
            self.assertEqual(
                [2, -1],
                sol.nextGreaterElements([1, 2]),
            )
        for sol in self.solutions:
            self.assertEqual(
                [-1, -1],
                sol.nextGreaterElements([2, 2]),
            )

    def test_negative_values(self):
        for sol in self.solutions:
            self.assertEqual(
                [0, 0, -1],
                sol.nextGreaterElements([-1, -3, 0]),
            )


if __name__ == "__main__":
    unittest.main()
