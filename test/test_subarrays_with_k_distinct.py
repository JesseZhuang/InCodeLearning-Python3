import unittest

from algorithm.sliding.subarrays_with_k_distinct import Solution


class TestSubarraysWithKDistinct(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.subarraysWithKDistinct([1, 2, 1, 2, 3], 2), 7)

    def test_example2(self):
        self.assertEqual(self.solution.subarraysWithKDistinct([1, 2, 1, 3, 4], 3), 3)

    def test_one_distinct_value(self):
        self.assertEqual(self.solution.subarraysWithKDistinct([1, 1, 1], 1), 6)

    def test_k_exceeds_number_of_distinct_values(self):
        self.assertEqual(self.solution.subarraysWithKDistinct([1, 2, 1], 3), 0)

    def test_k_equals_number_of_distinct_values(self):
        self.assertEqual(self.solution.subarraysWithKDistinct([1, 2, 3], 3), 1)

    def test_large_result_fits_integer_range(self):
        nums = [1] * 20_000
        self.assertEqual(self.solution.subarraysWithKDistinct(nums, 1), 200_010_000)


if __name__ == "__main__":
    unittest.main()
