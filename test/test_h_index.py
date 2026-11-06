import unittest

from algorithm.jzarray.h_index import Solution


class TestHIndex(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def verify(self, citations, expected):
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(solution.hIndex(citations[:]), expected)
                self.assertEqual(solution.hIndexSort(citations[:]), expected)

    def test_example_one(self):
        self.verify([3, 0, 6, 1, 5], 3)

    def test_example_two(self):
        self.verify([1, 3, 1], 1)

    def test_zero_citations(self):
        self.verify([0, 0, 0], 0)

    def test_every_paper_meets_n(self):
        self.verify([3, 3, 3], 3)

    def test_citations_capped_into_n_bucket(self):
        self.verify([1000], 1)

    def test_one_paper(self):
        self.verify([0], 0)


if __name__ == "__main__":
    unittest.main()
