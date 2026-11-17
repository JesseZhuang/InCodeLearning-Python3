import unittest

from algorithm.array.maximize_greatness import Solution


class TestMaximizeGreatness(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_official_examples_and_short_custom_case(self):
        cases = [
            ([1, 3, 5, 2, 1, 3, 1], 4),
            ([1, 2, 3, 4], 3),
            ([1, 3, 5, 2, 1], 3),
        ]
        for solution in self.solutions:
            for nums, expected in cases:
                with self.subTest(nums=nums):
                    self.assertEqual(expected, solution.maximizeGreatness(nums))

    def test_equal_values_cannot_create_greatness(self):
        for solution in self.solutions:
            self.assertEqual(0, solution.maximizeGreatness([7, 7, 7, 7]))

    def test_single_value(self):
        for solution in self.solutions:
            self.assertEqual(0, solution.maximizeGreatness([42]))

    def test_duplicate_values_are_matched_strictly(self):
        for solution in self.solutions:
            self.assertEqual(3, solution.maximizeGreatness([1, 1, 1, 2, 2, 3]))

    def test_large_values(self):
        for solution in self.solutions:
            self.assertEqual(
                2,
                solution.maximizeGreatness([1_000_000_000, 0, 1_000_000_000, 0]),
            )

    def test_maximum_length_shape(self):
        nums = [0] * 50_000 + [1] * 50_000
        for solution in self.solutions:
            self.assertEqual(50_000, solution.maximizeGreatness(nums.copy()))


if __name__ == "__main__":
    unittest.main()
