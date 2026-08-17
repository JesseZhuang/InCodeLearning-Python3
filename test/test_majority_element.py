import unittest

from algorithm.jzarray.majority_element import Solution


class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_single_element(self):
        for sol in self.solutions:
            self.assertEqual(sol.majorityElement([1]), 1)
            self.assertEqual(sol.majorityElementSort([1]), 1)

    def test_two_elements_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.majorityElement([2, 2]), 2)
            self.assertEqual(sol.majorityElementSort([2, 2]), 2)

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.majorityElement([3, 2, 3]), 3)
            self.assertEqual(sol.majorityElementSort([3, 2, 3]), 3)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
            self.assertEqual(sol.majorityElementSort([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.majorityElement([5, 5, 5, 5]), 5)
            self.assertEqual(sol.majorityElementSort([5, 5, 5, 5]), 5)

    def test_negative_numbers(self):
        for sol in self.solutions:
            self.assertEqual(sol.majorityElement([-1, -1, 2]), -1)
            self.assertEqual(sol.majorityElementSort([-1, -1, 2]), -1)

    def test_majority_at_end(self):
        for sol in self.solutions:
            self.assertEqual(sol.majorityElement([1, 2, 2, 2]), 2)
            self.assertEqual(sol.majorityElementSort([1, 2, 2, 2]), 2)

    def test_large_majority(self):
        for sol in self.solutions:
            nums = [7] * 5001 + list(range(4999))
            self.assertEqual(sol.majorityElement(nums), 7)
            self.assertEqual(sol.majorityElementSort(nums[:]), 7)


if __name__ == "__main__":
    unittest.main()
