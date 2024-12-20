from unittest import TestCase

from algorithm.jzstring.stickers_spell_word import Solution1, Solution2


class TestSolution(TestCase):
    def test_min_stickers(self):
        cases = [
            (['aa', 'b'], 'aaabbb', 5),
            (["heavy", "stone", "family", "had", "rain", "person", "verb", "clothe"], "overfresh", 4),
            (["with", "example", "science"], 'thehat', 3),
            (["notice", "possible"], 'basicbasic', -1),
            (["city", "would", "feel", "effect", "cell", "paint"], 'putcat', 3),
        ]
        tbt1, tbt2 = Solution1(), Solution2()
        for stickers, target, exp in cases:
            with self.subTest(stickers=stickers, target=target):
                self.assertEqual(exp, tbt1.minStickers(stickers, target))
                self.assertEqual(exp, tbt2.minStickers(stickers, target))
