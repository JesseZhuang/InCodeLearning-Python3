import unittest

from algorithm.stack.online_stock_span import StockSpanner, StockSpannerDP


class TestOnlineStockSpan(unittest.TestCase):
    def setUp(self):
        self.solutions = [StockSpanner, StockSpannerDP]

    def verify(self, prices, expected):
        for cls in self.solutions:
            with self.subTest(sol=cls.__name__):
                obj = cls()
                for price, exp in zip(prices, expected):
                    self.assertEqual(exp, obj.next(price))

    def test_example1(self):
        """LeetCode example: [100, 80, 60, 70, 60, 75, 85]."""
        self.verify(
            [100, 80, 60, 70, 60, 75, 85],
            [1, 1, 1, 2, 1, 4, 6],
        )

    def test_single_call(self):
        self.verify([50], [1])

    def test_all_increasing(self):
        """Each price is larger than the previous, span grows."""
        self.verify([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

    def test_all_decreasing(self):
        """Each price is smaller, span is always 1."""
        self.verify([5, 4, 3, 2, 1], [1, 1, 1, 1, 1])

    def test_all_same(self):
        """All same price, span grows linearly."""
        self.verify([10, 10, 10, 10], [1, 2, 3, 4])

    def test_valley_and_peak(self):
        """Price drops then rises above all."""
        self.verify([100, 50, 30, 20, 110], [1, 1, 1, 1, 5])

    def test_alternating(self):
        self.verify([10, 5, 10, 5, 10], [1, 1, 3, 1, 5])

    def test_constraint_min_max(self):
        """Test with constraint boundary values: 1 <= price <= 10^5."""
        self.verify([1, 100000, 1, 100000], [1, 2, 1, 4])
