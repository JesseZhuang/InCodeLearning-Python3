import unittest

from algorithm.hash.third_max import ThirdMax


class TestThirdMax(unittest.TestCase):
    """unit test"""

    def setUp(self) -> None:
        self.tbt = ThirdMax()

    def test_duplicate(self):
        self.assertEqual(1, self.tbt.third_max([2, 2, 3, 1]))

    def test_no_third(self):
        self.assertEqual(2, self.tbt.third_max([2, 1]))
