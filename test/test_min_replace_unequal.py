from unittest import TestCase

from algorithm.sliding.min_replace_unequal import minReplaceUnequal


class TestMinReplacementUnequal(TestCase):
    def test_min_replace_unequal(self):
        cases = [
            ('ab', 0),
            ('caaab', 1),
            ('xxxxxxx', 3),
            ('add', 1),
            ('boook', 1),
            ('break', 0),
            ('abaaaba', 1),
            ('abab', 0),
        ]
        for s, exp in cases:
            with self.subTest(s=s, exp=exp):
                self.assertEqual(exp, minReplaceUnequal(s))
