import unittest

from algorithm.jzstruct.list_node import ListNode
from algorithm.list.reorder_list import Solution, Solution2


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


class TestReorderList(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, vals, expected):
        for sol in self.solutions:
            head = build(vals)
            sol.reorderList(head)
            self.assertEqual(expected, to_list(head), f"{sol.__class__.__name__} {vals}")

    def test_example1(self):
        self.verify([1, 2, 3, 4], [1, 4, 2, 3])

    def test_example2(self):
        self.verify([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])

    def test_single(self):
        self.verify([1], [1])

    def test_two(self):
        self.verify([1, 2], [1, 2])

    def test_three(self):
        self.verify([1, 2, 3], [1, 3, 2])

    def test_six(self):
        self.verify([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4])

    def test_duplicates(self):
        self.verify([1, 1, 1, 1], [1, 1, 1, 1])

    def test_large_values(self):
        self.verify([1000, 999, 1, 500], [1000, 500, 999, 1])


if __name__ == '__main__':
    unittest.main()
