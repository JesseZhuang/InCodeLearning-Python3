import unittest
from algorithm.jzarray.find_all_duplicates import Solution, Solution2


class TestFindAllDuplicates(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def _assert(self, nums, expected):
        for sol in self.solutions:
            result = sorted(sol.findDuplicates(nums[:]))
            self.assertEqual(result, sorted(expected))

    def test_example1(self):
        self._assert([4, 3, 2, 7, 8, 2, 3, 1], [2, 3])

    def test_example2(self):
        self._assert([1, 1, 2], [1])

    def test_example3_no_duplicates(self):
        self._assert([1], [])

    def test_all_duplicates(self):
        self._assert([1, 2, 1, 2], [1, 2])

    def test_single_duplicate(self):
        self._assert([2, 2], [2])

    def test_no_duplicates_full(self):
        self._assert([1, 2, 3, 4, 5], [])

    def test_duplicate_at_boundaries(self):
        self._assert([1, 3, 4, 2, 1, 4], [1, 4])

    def test_large_values(self):
        self._assert([10, 2, 5, 10, 9, 1, 1, 4, 3, 7], [10, 1])

    def test_consecutive_duplicates(self):
        self._assert([3, 3, 1, 2], [3])

    def test_all_same_pair(self):
        self._assert([5, 5, 3, 3, 1, 1, 2, 4], [5, 3, 1])


if __name__ == "__main__":
    unittest.main()
