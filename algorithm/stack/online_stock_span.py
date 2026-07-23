class StockSpanner:
    """Monotonic decreasing stack approach.

    Stack stores (price, span) pairs. When a new price comes in,
    we pop all entries with price <= current and accumulate their spans.
    """

    def __init__(self):
        self.stack = []  # O(n) space

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:  # O(1) amortized, each element pushed/popped at most once
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


class StockSpannerDP:
    """DP-like approach using an array to jump backwards."""

    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        span = 1
        i = len(self.prices) - 2
        while i >= 0 and self.prices[i] <= price:  # O(n) worst case per call
            span += self.spans[i]
            i -= self.spans[i]  # jump backwards by span[i]
        self.spans.append(span)
        return span
