import unittest

from algorithm.jzarray.next_permutation import Solution


class TestNextPermutation(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            nums = [1, 2, 3]
            sol.nextPermutation(nums)
            self.assertEqual(nums, [1, 3, 2])

    def test_example2(self):
        for sol in self.solutions:
            nums = [3, 2, 1]
            sol.nextPermutation(nums)
            self.assertEqual(nums, [1, 2, 3])

    def test_example3(self):
        for sol in self.solutions:
            nums = [1, 1, 5]
            sol.nextPermutation(nums)
            self.assertEqual(nums, [1, 5, 1])

    def test_single_element(self):
        for sol in self.solutions:
            nums = [1]
            sol.nextPermutation(nums)
            self.assertEqual(nums, [1])

    def test_two_elements_ascending(self):
        for sol in self.solutions:
            nums = [1, 2]
            sol.nextPermutation(nums)
            self.assertEqual(nums, [2, 1])

    def test_two_elements_descending(self):
        for sol in self.solutions:
            nums = [2, 1]
            sol.nextPermutation(nums)
            self.assertEqual(nums, [1, 2])

    def test_duplicates(self):
        for sol in self.solutions:
            nums = [1, 2, 2]
            sol.nextPermutation(nums)
            self.assertEqual(nums, [2, 1, 2])

    def test_middle_pivot(self):
        for sol in self.solutions:
            nums = [1, 3, 2]
            sol.nextPermutation(nums)
            self.assertEqual(nums, [2, 1, 3])

    def test_longer_sequence(self):
        for sol in self.solutions:
            nums = [2, 3, 1, 3, 3]
            sol.nextPermutation(nums)
            self.assertEqual(nums, [2, 3, 3, 1, 3])


if __name__ == '__main__':
    unittest.main()
