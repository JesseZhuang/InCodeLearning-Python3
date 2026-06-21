import unittest

from algorithm.jzstruct.list_node import ListNode
from algorithm.list.reverse_nodes_in_k_group import Solution1, Solution2


def build(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


class TestReverseNodesInKGroup(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution1(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            head = build([1, 2, 3, 4, 5])
            result = sol.reverseKGroup(head, 2)
            self.assertEqual([2, 1, 4, 3, 5], to_list(result))

    def test_example2(self):
        for sol in self.solutions:
            head = build([1, 2, 3, 4, 5])
            result = sol.reverseKGroup(head, 3)
            self.assertEqual([3, 2, 1, 4, 5], to_list(result))

    def test_k_equals_1(self):
        for sol in self.solutions:
            head = build([1, 2, 3])
            result = sol.reverseKGroup(head, 1)
            self.assertEqual([1, 2, 3], to_list(result))

    def test_k_equals_length(self):
        for sol in self.solutions:
            head = build([1, 2, 3, 4])
            result = sol.reverseKGroup(head, 4)
            self.assertEqual([4, 3, 2, 1], to_list(result))

    def test_single_node(self):
        for sol in self.solutions:
            head = build([1])
            result = sol.reverseKGroup(head, 1)
            self.assertEqual([1], to_list(result))

    def test_k_larger_than_length(self):
        for sol in self.solutions:
            head = build([1, 2])
            result = sol.reverseKGroup(head, 3)
            self.assertEqual([1, 2], to_list(result))

    def test_empty_list(self):
        for sol in self.solutions:
            result = sol.reverseKGroup(None, 2)
            self.assertIsNone(result)

    def test_two_full_groups(self):
        for sol in self.solutions:
            head = build([1, 2, 3, 4, 5, 6])
            result = sol.reverseKGroup(head, 3)
            self.assertEqual([3, 2, 1, 6, 5, 4], to_list(result))


if __name__ == '__main__':
    unittest.main()
