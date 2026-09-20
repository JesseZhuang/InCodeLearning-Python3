import unittest

from algorithm.hash.sort_characters_by_frequency import Solution, Solution2


class TestSortCharactersByFrequency(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, s, expected_set):
        """Verify result matches one of the valid outputs (order among same-freq chars varies)."""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.frequencySort(s)
                self.assertIn(result, expected_set)

    def verify_by_freq(self, s):
        """Verify the result has correct character frequencies and is sorted by frequency."""
        from collections import Counter
        original_count = Counter(s)
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.frequencySort(s)
                self.assertEqual(Counter(result), original_count)
                # verify frequency ordering: chars appear in non-increasing frequency
                prev_freq = float('inf')
                i = 0
                while i < len(result):
                    c = result[i]
                    run_len = 0
                    while i < len(result) and result[i] == c:
                        run_len += 1
                        i += 1
                    self.assertEqual(run_len, original_count[c])
                    self.assertLessEqual(run_len, prev_freq)
                    prev_freq = run_len

    def test_example1(self):
        self.verify("tree", {"eert", "eetr"})

    def test_example2(self):
        self.verify("cccaaa", {"aaaccc", "cccaaa"})

    def test_example3(self):
        self.verify("Aabb", {"bbAa", "bbaA"})

    def test_single_char(self):
        self.verify("z", {"z"})

    def test_all_same(self):
        self.verify("aaaa", {"aaaa"})

    def test_all_unique(self):
        self.verify_by_freq("abc")

    def test_digits_and_letters(self):
        self.verify_by_freq("2a554442f544asfasssffffasss")

    def test_case_sensitive(self):
        # 'a' and 'A' are different characters
        self.verify("aAaA", {"aaAA", "AAaa"})

    def test_two_chars(self):
        self.verify("ab", {"ab", "ba"})

    def test_long_repeated(self):
        self.verify("bbbcccaaa", {"bbbcccaaa", "cccbbbaaaa"[:-1], "aaabbbccc", "aaacccbbb",
                                   "bbbaaaccc", "cccaaabbb"})


if __name__ == '__main__':
    unittest.main()
