import unittest

from algorithm.heap.hand_of_straights import Solution, Solution2


class TestHandOfStraights(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, hand, groupSize, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.isNStraightHand(hand, groupSize))

    def test_example1(self):
        self.verify([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True)

    def test_example2(self):
        self.verify([1, 2, 3, 4, 5], 4, False)

    def test_single_group(self):
        self.verify([1, 2, 3], 3, True)

    def test_single_card_groups(self):
        self.verify([5, 1, 3], 1, True)

    def test_not_enough_consecutive(self):
        self.verify([1, 2, 3, 4, 5, 7], 3, False)

    def test_duplicates_forming_groups(self):
        self.verify([1, 1, 2, 2, 3, 3], 3, True)

    def test_large_group_size(self):
        self.verify([1, 2, 3, 4, 5, 6, 7, 8], 8, True)

    def test_with_gap_but_valid(self):
        self.verify([1, 2, 4, 5], 2, True)

    def test_impossible_with_gap(self):
        self.verify([1, 3, 5, 7], 2, False)

    def test_empty_hand(self):
        self.verify([], 3, True)

    def test_indivisible_length(self):
        self.verify([1, 2, 3, 4], 3, False)


if __name__ == '__main__':
    unittest.main()
