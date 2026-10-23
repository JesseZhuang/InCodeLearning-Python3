import unittest

from algorithm.stack.remove_all_adjacent_duplicates_in_string import Solution


class TestRemoveAllAdjacentDuplicatesInString(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_examples(self):
        for solution in self.solutions:
            self.assertEqual(solution.removeDuplicates("abbaca"), "ca")
            self.assertEqual(solution.removeDuplicates("azxxzy"), "ay")

    def test_single_character_and_no_duplicates(self):
        for solution in self.solutions:
            self.assertEqual(solution.removeDuplicates("a"), "a")
            self.assertEqual(solution.removeDuplicates("abcd"), "abcd")

    def test_pairs_disappear(self):
        for solution in self.solutions:
            self.assertEqual(solution.removeDuplicates("aa"), "")
            self.assertEqual(solution.removeDuplicates("aabbcc"), "")

    def test_cascading_removals(self):
        for solution in self.solutions:
            self.assertEqual(solution.removeDuplicates("abba"), "")
            self.assertEqual(solution.removeDuplicates("abccba"), "")

    def test_maximum_length(self):
        for solution in self.solutions:
            self.assertEqual(solution.removeDuplicates("ab" * 50_000), "ab" * 50_000)
            self.assertEqual(solution.removeDuplicates("a" * 100_000), "")


if __name__ == "__main__":
    unittest.main()
