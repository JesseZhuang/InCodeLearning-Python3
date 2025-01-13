from unittest import TestCase

from algorithm.hash.programmer_strings import programmerStrings


class Test(TestCase):
    def test_programmer_strings(self):
        cases = [
            ('programmerxxxprozmerqgram', 3),
            ('progxrammerrxproxgrammer', 2),
            ('xprogxrmaxemrppprommograeiruu', 2),
            ('programmerprogrammer', 0)
        ]
        for s, exp in cases:
            with self.subTest(s=s, exp=exp):
                self.assertEqual(exp, programmerStrings(s))
