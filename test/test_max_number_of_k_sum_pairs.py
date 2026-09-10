import unittest

from algorithm.hash.max_number_of_k_sum_pairs import Solution, Solution2


class TestMaxOperations(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, nums, k, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.maxOperations(list(nums), k))

    def test_example1(self):
        self.verify([1, 2, 3, 4], 5, 2)

    def test_example2(self):
        self.verify([3, 1, 3, 4, 3], 6, 1)

    def test_no_pairs(self):
        self.verify([1, 1, 1], 10, 0)

    def test_all_pairs(self):
        self.verify([1, 3, 1, 3], 4, 2)

    def test_duplicate_elements(self):
        self.verify([2, 2, 2, 2], 4, 2)

    def test_single_element(self):
        self.verify([5], 5, 0)

    def test_two_elements_match(self):
        self.verify([1, 4], 5, 1)

    def test_two_elements_no_match(self):
        self.verify([1, 2], 5, 0)

    def test_large_k(self):
        self.verify([1, 2, 3, 4, 5], 100, 0)

    def test_negatives_not_applicable(self):
        """Constraints: 1 <= nums[i] <= 10^9, so all positive. Test boundary."""
        self.verify([1, 1, 1, 1, 1], 2, 2)

    def test_greedy_pairing(self):
        self.verify([3, 1, 5, 1, 3, 1], 4, 2)

    def test_odd_count_duplicates(self):
        self.verify([2, 2, 2], 4, 1)


if __name__ == '__main__':
    unittest.main()
