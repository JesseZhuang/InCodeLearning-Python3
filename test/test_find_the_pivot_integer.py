from unittest import TestCase

from algorithm.jzarray.find_the_pivot_integer import Solution


class TestFindThePivotInteger(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_examples_and_boundaries(self):
        for value, expected in [(1, 1), (2, -1), (4, -1), (8, 6), (49, 35), (1000, -1)]:
            for solution in self.solutions:
                with self.subTest(value=value, method="math"):
                    self.assertEqual(solution.pivotInteger(value), expected)
                with self.subTest(value=value, method="prefix"):
                    self.assertEqual(solution.pivotIntegerPrefixSum(value), expected)

    def test_methods_agree_for_every_valid_input(self):
        for solution in self.solutions:
            for value in range(1, 1001):
                with self.subTest(value=value):
                    self.assertEqual(
                        solution.pivotInteger(value),
                        solution.pivotIntegerPrefixSum(value),
                    )
