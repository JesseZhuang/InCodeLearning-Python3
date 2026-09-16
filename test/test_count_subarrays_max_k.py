import unittest

from algorithm.sliding.count_subarrays_max_k import Solution, Solution2


class TestCountSubarraysMaxK(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubarrays([1, 3, 2, 3, 3], 2), 6)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubarrays([1, 4, 2, 1], 3), 0)

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubarrays([5, 5, 5, 5], 2), 6)

    def test_single_element_k1(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubarrays([7], 1), 1)

    def test_max_at_ends(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubarrays([3, 1, 1, 3], 2), 1)

    def test_k_equals_total_max_count(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubarrays([2, 1, 2, 1, 2], 3), 1)

    def test_k1_all_valid(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubarrays([1, 2, 3], 1), 3)

    def test_large_k_no_valid(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubarrays([5, 1, 5, 1], 3), 0)

    def test_consecutive_max(self):
        for sol in self.solutions:
            self.assertEqual(sol.countSubarrays([4, 4, 4, 1, 1], 2), 7)


if __name__ == "__main__":
    unittest.main()
