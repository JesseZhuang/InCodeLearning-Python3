import unittest

from algorithm.list.palindrome_ll import Solution, Solution2
from algorithm.jzstruct.list_node import ListNode


def build(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


class TestPalindromeLL(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, vals, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.isPalindrome(build(vals)), expected)

    def test_even_palindrome(self):
        self.verify([1, 2, 2, 1], True)

    def test_not_palindrome(self):
        self.verify([1, 2], False)

    def test_single_node(self):
        self.verify([1], True)

    def test_odd_palindrome(self):
        self.verify([1, 2, 1], True)

    def test_odd_not_palindrome(self):
        self.verify([1, 2, 3], False)

    def test_all_same(self):
        self.verify([5, 5, 5, 5], True)

    def test_two_same(self):
        self.verify([1, 1], True)

    def test_long_palindrome(self):
        vals = list(range(1, 51)) + list(range(50, 0, -1))
        self.verify(vals, True)

    def test_long_not_palindrome(self):
        vals = list(range(1, 51)) + list(range(50, 0, -1))
        vals[50] = 999
        self.verify(vals, False)

    def test_boundary_values(self):
        self.verify([0, 9, 0], True)
        self.verify([0, 9, 1], False)
