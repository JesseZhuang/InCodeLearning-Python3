import unittest

from algorithm.dp.shopping_offers import Solution, Solution2


class TestShoppingOffers(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, price, special, needs, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.shoppingOffers(price, special, needs))

    def test_example1(self):
        self.verify([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2], 14)

    def test_example2(self):
        self.verify([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1], 11)

    def test_no_offers(self):
        self.verify([1, 2, 3], [], [3, 2, 1], 10)

    def test_no_needs(self):
        self.verify([10, 20], [[1, 1, 5]], [0, 0], 0)

    def test_single_item(self):
        self.verify([5], [[2, 8]], [4], 16)

    def test_offer_worse_than_individual(self):
        """Offer costs more than buying individually — should be filtered out."""
        self.verify([1, 1], [[1, 1, 5]], [2, 2], 4)

    def test_multiple_same_offer(self):
        self.verify([4, 3], [[2, 1, 5]], [4, 2], 10)

    def test_offer_exact_match(self):
        self.verify([10, 10], [[1, 1, 1]], [1, 1], 1)

    def test_large_needs_single_item(self):
        self.verify([3], [[2, 5]], [6], 15)

    def test_mixed_offers(self):
        self.verify([2, 3], [[1, 0, 1], [0, 1, 2], [1, 1, 3]], [2, 2], 6)

    def test_needs_one_each(self):
        self.verify([5, 5, 5], [[1, 1, 1, 10]], [1, 1, 1], 10)
