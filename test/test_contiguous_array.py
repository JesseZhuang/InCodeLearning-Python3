import unittest

from algorithm.hash.contiguous_array import Solution


class TestContiguousArray(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.findMaxLength([0, 1]), 2)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.findMaxLength([0, 1, 0]), 2)

    def test_all_zeros(self):
        for sol in self.solutions:
            self.assertEqual(sol.findMaxLength([0, 0, 0]), 0)

    def test_all_ones(self):
        for sol in self.solutions:
            self.assertEqual(sol.findMaxLength([1, 1, 1]), 0)

    def test_entire_array(self):
        for sol in self.solutions:
            self.assertEqual(sol.findMaxLength([0, 1, 1, 0]), 4)

    def test_longer(self):
        for sol in self.solutions:
            self.assertEqual(sol.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]), 6)

    def test_single_element(self):
        for sol in self.solutions:
            self.assertEqual(sol.findMaxLength([0]), 0)
            self.assertEqual(sol.findMaxLength([1]), 0)

    def test_alternating(self):
        for sol in self.solutions:
            self.assertEqual(sol.findMaxLength([0, 1, 0, 1, 0, 1]), 6)


if __name__ == "__main__":
    unittest.main()
