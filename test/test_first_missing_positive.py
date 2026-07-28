import unittest

from algorithm.jzarray.first_missing_positive import Solution


class TestFirstMissingPositive(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.firstMissingPositive([1, 2, 0]), 3)
            self.assertEqual(sol.firstMissingPositive2([1, 2, 0]), 3)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.firstMissingPositive([3, 4, -1, 1]), 2)
            self.assertEqual(sol.firstMissingPositive2([3, 4, -1, 1]), 2)

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(sol.firstMissingPositive([7, 8, 9, 11, 12]), 1)
            self.assertEqual(sol.firstMissingPositive2([7, 8, 9, 11, 12]), 1)

    def test_single_element(self):
        for sol in self.solutions:
            self.assertEqual(sol.firstMissingPositive([1]), 2)
            self.assertEqual(sol.firstMissingPositive2([1]), 2)
            self.assertEqual(sol.firstMissingPositive([2]), 1)
            self.assertEqual(sol.firstMissingPositive2([2]), 1)

    def test_consecutive_from_one(self):
        for sol in self.solutions:
            self.assertEqual(sol.firstMissingPositive([1, 2, 3, 4, 5]), 6)
            self.assertEqual(sol.firstMissingPositive2([1, 2, 3, 4, 5]), 6)

    def test_duplicates(self):
        for sol in self.solutions:
            self.assertEqual(sol.firstMissingPositive([1, 1, 1, 1]), 2)
            self.assertEqual(sol.firstMissingPositive2([1, 1, 1, 1]), 2)

    def test_all_negative(self):
        for sol in self.solutions:
            self.assertEqual(sol.firstMissingPositive([-1, -2, -3]), 1)
            self.assertEqual(sol.firstMissingPositive2([-1, -2, -3]), 1)

    def test_large_values(self):
        for sol in self.solutions:
            self.assertEqual(sol.firstMissingPositive([2**31 - 1, -2**31, 1, 2]), 3)
            self.assertEqual(sol.firstMissingPositive2([2**31 - 1, -2**31, 1, 2]), 3)


if __name__ == "__main__":
    unittest.main()
