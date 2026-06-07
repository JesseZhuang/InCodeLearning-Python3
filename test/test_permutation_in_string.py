import unittest

from algorithm.sliding.permutation_in_string import Solution, Solution2


class TestPermutationInString(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_basic_true(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.checkInclusion("ab", "eidbaooo"))

    def test_basic_false(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertFalse(sol.checkInclusion("ab", "eidboaoo"))

    def test_s1_longer_than_s2(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertFalse(sol.checkInclusion("abcdef", "ab"))

    def test_exact_match(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.checkInclusion("abc", "cba"))

    def test_single_char_present(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.checkInclusion("a", "a"))

    def test_single_char_absent(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertFalse(sol.checkInclusion("a", "b"))

    def test_permutation_at_end(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.checkInclusion("adc", "dcda"))

    def test_all_same_chars(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.checkInclusion("aaa", "aaaa"))

    def test_no_permutation_all_same(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertFalse(sol.checkInclusion("ab", "aaaa"))


if __name__ == '__main__':
    unittest.main()
