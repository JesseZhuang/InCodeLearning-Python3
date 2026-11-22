import unittest

from algorithm.array.arithmetic_triplets import Solution


class TestArithmeticTriplets(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_first_official_example(self):
        for solution in self.solutions:
            self.assertEqual(
                solution.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3), 2
            )

    def test_second_official_example(self):
        for solution in self.solutions:
            self.assertEqual(solution.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2), 2)

    def test_returns_zero_when_no_triplets_exist(self):
        for solution in self.solutions:
            self.assertEqual(solution.arithmeticTriplets([0, 1, 2, 3, 4], 3), 0)

    def test_counts_overlapping_triplets(self):
        for solution in self.solutions:
            self.assertEqual(solution.arithmeticTriplets([0, 1, 2, 3, 4], 1), 3)

    def test_minimum_length_and_maximum_values(self):
        for solution in self.solutions:
            self.assertEqual(solution.arithmeticTriplets([100, 150, 200], 50), 1)


if __name__ == "__main__":
    unittest.main()
