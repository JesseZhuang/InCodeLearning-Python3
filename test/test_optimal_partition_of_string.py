import unittest

from algorithm.string.optimal_partition_of_string import Solution, Solution2


class TestOptimalPartitionOfString(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def assertBoth(self, s, expected):
        for solution in self.solutions:
            self.assertEqual(expected, solution.partitionString(s))

    def test_examples(self):
        self.assertBoth("abacaba", 4)
        self.assertBoth("ssssss", 6)

    def test_single_character(self):
        self.assertBoth("s", 1)

    def test_all_lowercase_letters_are_unique(self):
        self.assertBoth("abcdefghijklmnopqrstuvwxyz", 1)

    def test_duplicate_after_full_alphabet_starts_new_partition(self):
        self.assertBoth("abcdefghijklmnopqrstuvwxyzabc", 2)

    def test_maximum_length_repeated_input(self):
        self.assertBoth("a" * 100000, 100000)


if __name__ == "__main__":
    unittest.main()
