from unittest import TestCase

from algorithm.math.reverse_count_say import Solution


class TestReverseCountSay(TestCase):

    def test_reverse_count_say(self):
        tbt = Solution()
        self.assertEqual("111221", tbt.reverseCountSay("312211"))
