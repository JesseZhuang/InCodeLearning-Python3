import unittest

from algorithm.jzstring.minimum_deletions_to_make_string_balanced import Solution


class TestMinimumDeletionsToMakeStringBalanced(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.methods = [
            self.solution.minimumDeletions,
            self.solution.minimumDeletionsBySplit,
        ]

    def test_examples_and_edge_cases(self):
        cases = [
            ("a", 0),
            ("b", 0),
            ("", 0),
            ("aaabbb", 0),
            ("aabb", 0),
            ("ba", 1),
            ("bba", 1),
            ("aababb", 1),
            ("bbaaaaabb", 2),
            ("babaa", 2),
            ("bbbbaaaa", 4),
        ]
        for method in self.methods:
            for text, expected in cases:
                with self.subTest(method=method.__name__, text=text):
                    self.assertEqual(expected, method(text))

    def test_maximum_length_pattern(self):
        text = "b" * 50_000 + "a" * 50_000
        for method in self.methods:
            with self.subTest(method=method.__name__):
                self.assertEqual(50_000, method(text))


if __name__ == "__main__":
    unittest.main()
