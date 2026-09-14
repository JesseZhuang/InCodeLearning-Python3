import unittest

from algorithm.sliding.fruit_into_baskets import Solution, Solution2


class TestFruitIntoBaskets(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, fruits, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.totalFruit(fruits[:]), expected)

    def test_example1(self):
        self.verify([1, 2, 1], 3)

    def test_example2(self):
        self.verify([0, 1, 2, 2], 3)

    def test_example3(self):
        self.verify([1, 2, 3, 2, 2], 4)

    def test_single_element(self):
        self.verify([1], 1)

    def test_all_same(self):
        self.verify([5, 5, 5, 5], 4)

    def test_two_types(self):
        self.verify([1, 2, 1, 2, 1], 5)

    def test_three_types_at_boundary(self):
        self.verify([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5)

    def test_alternating_three(self):
        self.verify([1, 2, 3, 1, 2, 3], 2)

    def test_long_run_then_switch(self):
        self.verify([1, 1, 1, 1, 2, 3, 3, 3], 5)

    def test_two_elements(self):
        self.verify([1, 2], 2)


if __name__ == "__main__":
    unittest.main()
