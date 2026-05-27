import unittest

from algorithm.binary_search.find_peak_element import Solution


class TestFindPeakElement(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def _is_peak(self, nums, idx):
        if idx < 0 or idx >= len(nums):
            return False
        left_ok = idx == 0 or nums[idx] > nums[idx - 1]
        right_ok = idx == len(nums) - 1 or nums[idx] > nums[idx + 1]
        return left_ok and right_ok

    def test_single_element(self):
        for sol in self.solutions:
            self.assertEqual(sol.find_peak_element([1]), 0)
            self.assertEqual(sol.find_peak_element_linear([1]), 0)

    def test_two_elements_ascending(self):
        for sol in self.solutions:
            self.assertEqual(sol.find_peak_element([1, 2]), 1)
            self.assertEqual(sol.find_peak_element_linear([1, 2]), 1)

    def test_two_elements_descending(self):
        for sol in self.solutions:
            self.assertEqual(sol.find_peak_element([2, 1]), 0)
            self.assertEqual(sol.find_peak_element_linear([2, 1]), 0)

    def test_example1(self):
        nums = [1, 2, 3, 1]
        for sol in self.solutions:
            self.assertTrue(self._is_peak(nums, sol.find_peak_element(nums)))
            self.assertTrue(self._is_peak(nums, sol.find_peak_element_linear(nums)))

    def test_example2(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        for sol in self.solutions:
            self.assertTrue(self._is_peak(nums, sol.find_peak_element(nums)))
            self.assertTrue(self._is_peak(nums, sol.find_peak_element_linear(nums)))

    def test_ascending(self):
        nums = [1, 2, 3, 4, 5]
        for sol in self.solutions:
            self.assertEqual(sol.find_peak_element(nums), 4)
            self.assertEqual(sol.find_peak_element_linear(nums), 4)

    def test_descending(self):
        nums = [5, 4, 3, 2, 1]
        for sol in self.solutions:
            self.assertEqual(sol.find_peak_element(nums), 0)
            self.assertEqual(sol.find_peak_element_linear(nums), 0)

    def test_multiple_peaks(self):
        nums = [1, 3, 2, 4, 1]
        for sol in self.solutions:
            self.assertTrue(self._is_peak(nums, sol.find_peak_element(nums)))
            self.assertTrue(self._is_peak(nums, sol.find_peak_element_linear(nums)))


if __name__ == "__main__":
    unittest.main()
