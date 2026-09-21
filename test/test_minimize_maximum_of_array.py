from unittest import TestCase

from algorithm.jzarray.minimize_maximum_of_array import Solution, Solution2


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.minimizeArrayValue([3, 7, 1, 6]), 5)

    def test_example2(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.minimizeArrayValue([10, 1]), 10)

    def test_single_element(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.minimizeArrayValue([5]), 5)

    def test_all_same(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.minimizeArrayValue([4, 4, 4, 4]), 4)

    def test_descending(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.minimizeArrayValue([10, 5, 1]), 10)

    def test_ascending(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.minimizeArrayValue([1, 5, 10]), 6)

    def test_all_zeros(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.minimizeArrayValue([0, 0, 0]), 0)

    def test_large_first(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.minimizeArrayValue([0, 0, 0, 0, 100]), 20)

    def test_two_elements_even(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.minimizeArrayValue([1, 9]), 5)

    def test_two_elements_odd(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.minimizeArrayValue([1, 10]), 6)
