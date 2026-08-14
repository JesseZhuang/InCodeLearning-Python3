import unittest

from algorithm.binary_search.successful_pairs_of_spells_and_potions import Solution


class TestSuccessfulPairs(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual([4, 0, 3], sol.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual([2, 0, 2], sol.successfulPairs([3, 1, 2], [8, 5, 8], 16))

    def test_single_spell_single_potion_success(self):
        for sol in self.solutions:
            self.assertEqual([1], sol.successfulPairs([10], [10], 100))

    def test_single_spell_single_potion_fail(self):
        for sol in self.solutions:
            self.assertEqual([0], sol.successfulPairs([10], [10], 101))

    def test_all_pairs_successful(self):
        for sol in self.solutions:
            self.assertEqual([3], sol.successfulPairs([100], [1, 2, 3], 1))

    def test_no_pairs_successful(self):
        for sol in self.solutions:
            self.assertEqual([0, 0], sol.successfulPairs([1, 1], [1, 1, 1], 5))

    def test_large_values_no_overflow(self):
        for sol in self.solutions:
            # spell=10^5, potion=10^5, success=10^10 => exactly meets threshold
            self.assertEqual([1], sol.successfulPairs([100000], [100000], 10000000000))

    def test_spell_equals_one(self):
        for sol in self.solutions:
            # need potion >= 7
            self.assertEqual([2], sol.successfulPairs([1], [5, 6, 7, 8], 7))


if __name__ == '__main__':
    unittest.main()
