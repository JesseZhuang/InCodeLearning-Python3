import unittest

from algorithm.jzarray.sort_colors import Solution, Solution2


class TestSortColors(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            nums = [2, 0, 2, 1, 1, 0]
            sol.sortColors(nums)
            self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_example2(self):
        for sol in self.solutions:
            nums = [2, 0, 1]
            sol.sortColors(nums)
            self.assertEqual(nums, [0, 1, 2])

    def test_single_element(self):
        for sol in self.solutions:
            for color in [0, 1, 2]:
                nums = [color]
                sol.sortColors(nums)
                self.assertEqual(nums, [color])

    def test_all_same(self):
        for sol in self.solutions:
            nums = [1, 1, 1]
            sol.sortColors(nums)
            self.assertEqual(nums, [1, 1, 1])

    def test_already_sorted(self):
        for sol in self.solutions:
            nums = [0, 0, 1, 1, 2, 2]
            sol.sortColors(nums)
            self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_reverse_sorted(self):
        for sol in self.solutions:
            nums = [2, 2, 1, 1, 0, 0]
            sol.sortColors(nums)
            self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_two_elements(self):
        for sol in self.solutions:
            nums = [1, 0]
            sol.sortColors(nums)
            self.assertEqual(nums, [0, 1])

    def test_no_ones(self):
        for sol in self.solutions:
            nums = [2, 0, 2, 0]
            sol.sortColors(nums)
            self.assertEqual(nums, [0, 0, 2, 2])

    def test_no_zeros(self):
        for sol in self.solutions:
            nums = [2, 1, 2, 1]
            sol.sortColors(nums)
            self.assertEqual(nums, [1, 1, 2, 2])

    def test_no_twos(self):
        for sol in self.solutions:
            nums = [1, 0, 1, 0]
            sol.sortColors(nums)
            self.assertEqual(nums, [0, 0, 1, 1])


if __name__ == "__main__":
    unittest.main()
