import unittest

from algorithm.jzarray.two_sum_ii import Solution, Solution2


class TestTwoSumII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual([1, 2], s.twoSum([2, 7, 11, 15], 9))

    def test_example2(self):
        for s in self.solutions:
            self.assertEqual([1, 3], s.twoSum([2, 3, 4], 6))

    def test_example3(self):
        for s in self.solutions:
            self.assertEqual([1, 2], s.twoSum([-1, 0], -1))

    def test_duplicates(self):
        for s in self.solutions:
            self.assertEqual([1, 2], s.twoSum([3, 3], 6))

    def test_negative_numbers(self):
        for s in self.solutions:
            self.assertEqual([1, 5], s.twoSum([-10, -5, -3, 0, 7], -3))

    def test_large_range(self):
        for s in self.solutions:
            self.assertEqual([1, 2], s.twoSum([-1000, 1000], 0))

    def test_target_with_first_last(self):
        for s in self.solutions:
            self.assertEqual([1, 4], s.twoSum([1, 2, 3, 4], 5))

    def test_adjacent_elements(self):
        for s in self.solutions:
            self.assertEqual([2, 3], s.twoSum([1, 3, 4, 7, 11], 7))

    def test_middle_pair(self):
        for s in self.solutions:
            self.assertEqual([2, 5], s.twoSum([1, 3, 5, 7, 9], 12))

    def test_two_elements(self):
        for s in self.solutions:
            self.assertEqual([1, 2], s.twoSum([0, 0], 0))


if __name__ == "__main__":
    unittest.main()
