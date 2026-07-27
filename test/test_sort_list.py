import unittest

from algorithm.jzstruct.list_node import ListNode
from algorithm.list.sort_list import Solution, Solution2


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


class TestSortList(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, vals, expected):
        for sol in self.solutions:
            head = build(vals)
            result = sol.sortList(head)
            self.assertEqual(expected, to_list(result), f"{sol.__class__.__name__} {vals}")

    def test_example1(self):
        self.verify([4, 2, 1, 3], [1, 2, 3, 4])

    def test_example2(self):
        self.verify([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5])

    def test_empty(self):
        self.verify([], [])

    def test_single(self):
        self.verify([1], [1])

    def test_two_sorted(self):
        self.verify([1, 2], [1, 2])

    def test_two_unsorted(self):
        self.verify([2, 1], [1, 2])

    def test_duplicates(self):
        self.verify([3, 1, 2, 3, 1], [1, 1, 2, 3, 3])

    def test_all_same(self):
        self.verify([5, 5, 5, 5], [5, 5, 5, 5])

    def test_already_sorted(self):
        self.verify([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.verify([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])

    def test_negative_values(self):
        self.verify([-100000, 100000, 0], [-100000, 0, 100000])


if __name__ == '__main__':
    unittest.main()
