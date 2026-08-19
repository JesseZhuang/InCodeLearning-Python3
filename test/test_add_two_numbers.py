import unittest

from algorithm.jzstruct.list_node import ListNode
from algorithm.linked_list.add_two_numbers import Solution


def to_linked_list(nums):
    """Convert a list of digits (reverse order) to a linked list."""
    dummy = ListNode()
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next


def to_list(head):
    """Convert a linked list to a Python list of values."""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def _run(self, l1_vals, l2_vals, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__, method="iterative"):
                l1 = to_linked_list(l1_vals)
                l2 = to_linked_list(l2_vals)
                result = sol.add_two_numbers(l1, l2)
                self.assertEqual(to_list(result), expected)
            with self.subTest(sol=sol.__class__.__name__, method="recursive"):
                l1 = to_linked_list(l1_vals)
                l2 = to_linked_list(l2_vals)
                result = sol.add_two_numbers_recursive(l1, l2)
                self.assertEqual(to_list(result), expected)

    def test_example1(self):
        # 342 + 465 = 807
        self._run([2, 4, 3], [5, 6, 4], [7, 0, 8])

    def test_both_zeros(self):
        self._run([0], [0], [0])

    def test_single_digits(self):
        # 3 + 4 = 7
        self._run([3], [4], [7])

    def test_single_digits_with_carry(self):
        # 5 + 7 = 12
        self._run([5], [7], [2, 1])

    def test_carry_propagation(self):
        # 999 + 1 = 1000
        self._run([9, 9, 9], [1], [0, 0, 0, 1])

    def test_different_lengths(self):
        # 99 + 1 = 100
        self._run([9, 9], [1], [0, 0, 1])

    def test_large_carry_propagation(self):
        # 9999999 + 9999999 = 19999998
        self._run(
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9, 9],
            [8, 9, 9, 9, 9, 9, 9, 1],
        )


if __name__ == "__main__":
    unittest.main()
