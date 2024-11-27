from unittest import TestCase

from algorithm.jzmath.reverse_count_say import Solution


class TestReverseCountSay(TestCase):

    def test_reverse_count_say(self):
        tbt = Solution()
        self.assertEqual("111221", tbt.reverseCountSay("312211"))
