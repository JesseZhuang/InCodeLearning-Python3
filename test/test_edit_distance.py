from unittest import TestCase

from algorithm.dp.edit_distance import Solution, Solution2


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_min_distance(self):
        cases = [
            ("horse", "ros", 3),
            ("intention", "execution", 5),
            ("", "", 0),
            ("", "abc", 3),
            ("abc", "", 3),
            ("abc", "abc", 0),
            ("a", "b", 1),
            ("kitten", "sitting", 3),
            ("sunday", "saturday", 3),
            ("dinitrophenylhydrazine", "acetylaminophenol", 19),
        ]
        for sol in self.solutions:
            for word1, word2, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, w1=word1, w2=word2):
                    self.assertEqual(sol.minDistance(word1, word2), exp)
