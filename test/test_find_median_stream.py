import unittest

from algorithm.heap.find_median_stream import MedianFinder, MedianFinderSorted


class TestFindMedianStream(unittest.TestCase):
    def setUp(self):
        self.solutions = [MedianFinder, MedianFinderSorted]

    def _run(self, cls, ops, vals, expected):
        obj = cls()
        for op, val, exp in zip(ops[1:], vals[1:], expected[1:]):
            if op == "addNum":
                obj.addNum(val[0])
            elif op == "findMedian":
                self.assertAlmostEqual(obj.findMedian(), exp)

    def test_example1(self):
        ops = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
        vals = [[], [1], [2], [], [3], []]
        expected = [None, None, None, 1.5, None, 2.0]
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                self._run(cls, ops, vals, expected)

    def test_single_element(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                obj = cls()
                obj.addNum(5)
                self.assertAlmostEqual(obj.findMedian(), 5.0)

    def test_two_elements(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                obj = cls()
                obj.addNum(1)
                obj.addNum(2)
                self.assertAlmostEqual(obj.findMedian(), 1.5)

    def test_negative_numbers(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                obj = cls()
                for num in [-5, -3, -1, 0, 2]:
                    obj.addNum(num)
                self.assertAlmostEqual(obj.findMedian(), -1.0)

    def test_duplicates(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                obj = cls()
                for num in [5, 5, 5, 5]:
                    obj.addNum(num)
                self.assertAlmostEqual(obj.findMedian(), 5.0)

    def test_large_range(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                obj = cls()
                for num in [-100000, 100000]:
                    obj.addNum(num)
                self.assertAlmostEqual(obj.findMedian(), 0.0)

    def test_incremental_median(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                obj = cls()
                obj.addNum(6)
                self.assertAlmostEqual(obj.findMedian(), 6.0)
                obj.addNum(10)
                self.assertAlmostEqual(obj.findMedian(), 8.0)
                obj.addNum(2)
                self.assertAlmostEqual(obj.findMedian(), 6.0)
                obj.addNum(6)
                self.assertAlmostEqual(obj.findMedian(), 6.0)


if __name__ == "__main__":
    unittest.main()
