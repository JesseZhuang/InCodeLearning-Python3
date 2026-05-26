import unittest
from algorithm.jzarray.find_duplicate_number import Solution, Solution2


class TestFindDuplicateNumber(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_basic_duplicate_at_end(self):
        for sol in self.solutions:
            self.assertEqual(sol.findDuplicate([1, 3, 4, 2, 2]), 2)

    def test_basic_duplicate_at_start(self):
        for sol in self.solutions:
            self.assertEqual(sol.findDuplicate([3, 1, 3, 4, 2]), 3)

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.findDuplicate([1, 1, 1, 1, 1]), 1)

    def test_two_elements(self):
        for sol in self.solutions:
            self.assertEqual(sol.findDuplicate([1, 1]), 1)

    def test_duplicate_appears_many_times(self):
        for sol in self.solutions:
            self.assertEqual(sol.findDuplicate([2, 2, 2, 2, 2]), 2)

    def test_large_value_duplicate(self):
        for sol in self.solutions:
            self.assertEqual(sol.findDuplicate([1, 4, 4, 2, 3]), 4)

    def test_sequential_with_dup(self):
        for sol in self.solutions:
            self.assertEqual(sol.findDuplicate([1, 2, 3, 4, 4]), 4)

    def test_duplicate_at_boundary(self):
        for sol in self.solutions:
            # n=5, values in [1,5], 6 elements
            self.assertEqual(sol.findDuplicate([5, 1, 2, 3, 4, 5]), 5)


if __name__ == "__main__":
    unittest.main()
