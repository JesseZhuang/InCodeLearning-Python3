import unittest

from algorithm.jzstring.kth_distinct_string import Solution


class TestKthDistinctString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        self.assertEqual(
            "a", self.solution.kthDistinct(["d", "b", "c", "b", "c", "a"], 2)
        )

    def test_example_two(self):
        self.assertEqual("aaa", self.solution.kthDistinct(["aaa", "aa", "a"], 1))

    def test_last_distinct_string(self):
        self.assertEqual("b", self.solution.kthDistinct(["a", "a", "b"], 1))

    def test_not_enough_distinct_strings(self):
        self.assertEqual("", self.solution.kthDistinct(["a", "b", "a"], 2))

    def test_no_distinct_strings(self):
        self.assertEqual("", self.solution.kthDistinct(["x", "x"], 1))

    def test_single_distinct_string(self):
        self.assertEqual("only", self.solution.kthDistinct(["only"], 1))


if __name__ == "__main__":
    unittest.main()
