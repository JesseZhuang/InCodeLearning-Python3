import unittest

from algorithm.jzstruct.list_node import ListNode
from algorithm.list.remove_nth_from_end import Solution, Solution2


def build(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


class TestRemoveNthFromEnd(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, vals, n, expected):
        for sol in self.solutions:
            head = build(vals)
            result = sol.removeNthFromEnd(head, n)
            self.assertEqual(expected, to_list(result), f"{sol.__class__.__name__} {vals} n={n}")

    def test_example1(self):
        self.verify([1, 2, 3, 4, 5], 2, [1, 2, 3, 5])

    def test_example2(self):
        self.verify([1], 1, [])

    def test_example3(self):
        self.verify([1, 2], 1, [1])

    def test_remove_head(self):
        self.verify([1, 2], 2, [2])

    def test_remove_middle(self):
        self.verify([1, 2, 3], 2, [1, 3])

    def test_single_element(self):
        self.verify([7], 1, [])

    def test_long_list_remove_last(self):
        self.verify(list(range(1, 11)), 1, list(range(1, 10)))

    def test_long_list_remove_first(self):
        self.verify(list(range(1, 11)), 10, list(range(2, 11)))


if __name__ == '__main__':
    unittest.main()
