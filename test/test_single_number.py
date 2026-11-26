import unittest

from algorithm.bit.single_number import Solution, Solution2


class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_finds_single_value_among_pairs(self):
        for solution in self.solutions:
            self.assertEqual(solution.singleNumber([2, 2, 1]), 1)
            self.assertEqual(solution.singleNumber([4, 1, 2, 1, 2]), 4)

    def test_handles_single_element(self):
        for solution in self.solutions:
            self.assertEqual(solution.singleNumber([7]), 7)

    def test_handles_negative_values_and_zero(self):
        for solution in self.solutions:
            self.assertEqual(solution.singleNumber([-1, -1, -7]), -7)
            self.assertEqual(solution.singleNumber([0, 2, 2]), 0)


if __name__ == "__main__":
    unittest.main()
