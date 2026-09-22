import unittest

from algorithm.jzarray.majority_element_ii import Solution


class TestMajorityElementII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sorted(sol.majorityElement([3, 2, 3])), [3])
            self.assertEqual(sorted(sol.majorityElementMap([3, 2, 3])), [3])

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sorted(sol.majorityElement([1, 1, 1, 3, 3, 2, 2, 2])), [1, 2])
            self.assertEqual(sorted(sol.majorityElementMap([1, 1, 1, 3, 3, 2, 2, 2])), [1, 2])

    def test_single_element(self):
        for sol in self.solutions:
            self.assertEqual(sol.majorityElement([1]), [1])
            self.assertEqual(sol.majorityElementMap([1]), [1])

    def test_two_elements(self):
        for sol in self.solutions:
            self.assertEqual(sorted(sol.majorityElement([1, 2])), [1, 2])
            self.assertEqual(sorted(sol.majorityElementMap([1, 2])), [1, 2])

    def test_no_majority(self):
        for sol in self.solutions:
            self.assertEqual(sol.majorityElement([1, 2, 3]), [])
            self.assertEqual(sol.majorityElementMap([1, 2, 3]), [])

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.majorityElement([5, 5, 5]), [5])
            self.assertEqual(sol.majorityElementMap([5, 5, 5]), [5])

    def test_negative_numbers(self):
        for sol in self.solutions:
            self.assertEqual(sorted(sol.majorityElement([-1, -1, -2, -2, 3])), [-2, -1])
            self.assertEqual(sorted(sol.majorityElementMap([-1, -1, -2, -2, 3])), [-2, -1])

    def test_exact_threshold_not_included(self):
        """n=6, threshold=2, element appearing exactly 2 times should NOT be included."""
        for sol in self.solutions:
            self.assertEqual(sorted(sol.majorityElement([1, 1, 2, 2, 3, 3])), [])
            self.assertEqual(sorted(sol.majorityElementMap([1, 1, 2, 2, 3, 3])), [])

    def test_large_input(self):
        for sol in self.solutions:
            nums = [7] * 4000 + [8] * 3500 + list(range(2500))
            self.assertEqual(sorted(sol.majorityElement(nums)), [7, 8])
            self.assertEqual(sorted(sol.majorityElementMap(nums)), [7, 8])

    def test_one_majority_out_of_many(self):
        for sol in self.solutions:
            self.assertEqual(sol.majorityElement([1, 2, 3, 1, 1, 1]), [1])
            self.assertEqual(sol.majorityElementMap([1, 2, 3, 1, 1, 1]), [1])


if __name__ == "__main__":
    unittest.main()
