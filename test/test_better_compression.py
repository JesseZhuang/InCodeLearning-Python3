from unittest import TestCase

from algorithm.hash.better_compression import better_compression


class Test(TestCase):
    def test_better_compression(self):
        cases = [
            ('a3c9b2c1', 'a3b2c10'),
            ('a12b56c1', 'a12b56c1'),
            ('a12c56a1b5', 'a13b5c56'),
            ('c2b3a1', 'a1b3c2'),
            ('a2b4c1', 'a2b4c1'),
        ]
        for s, exp in cases:
            with self.subTest(s=s):
                self.assertEqual(exp, better_compression(s))
