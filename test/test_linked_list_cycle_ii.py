import unittest

from algorithm.linked_list.linked_list_cycle_ii import Solution, Solution2
from algorithm.jzstruct.list_node import ListNode


def build_cycle_list(values, pos):
    """Build a linked list from values with cycle at pos (-1 for no cycle)."""
    if not values:
        return None, None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    cycle_node = None
    if pos >= 0:
        nodes[-1].next = nodes[pos]
        cycle_node = nodes[pos]
    return nodes[0], cycle_node


class TestLinkedListCycleII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1_cycle_at_1(self):
        """[3,2,0,-4], pos=1 -> node with val 2"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                head, expected = build_cycle_list([3, 2, 0, -4], 1)
                self.assertIs(sol.detectCycle(head), expected)

    def test_example2_cycle_at_0(self):
        """[1,2], pos=0 -> node with val 1"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                head, expected = build_cycle_list([1, 2], 0)
                self.assertIs(sol.detectCycle(head), expected)

    def test_example3_no_cycle(self):
        """[1], pos=-1 -> None"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                head, _ = build_cycle_list([1], -1)
                self.assertIsNone(sol.detectCycle(head))

    def test_empty_list(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertIsNone(sol.detectCycle(None))

    def test_single_node_self_cycle(self):
        """[1], pos=0 -> node with val 1"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                head, expected = build_cycle_list([1], 0)
                self.assertIs(sol.detectCycle(head), expected)

    def test_long_tail_short_cycle(self):
        """[1,2,3,4,5], pos=3 -> node with val 4"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                head, expected = build_cycle_list([1, 2, 3, 4, 5], 3)
                self.assertIs(sol.detectCycle(head), expected)

    def test_cycle_at_last_node(self):
        """[1,2,3], pos=2 -> node with val 3 (self-loop at tail)"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                head, expected = build_cycle_list([1, 2, 3], 2)
                self.assertIs(sol.detectCycle(head), expected)

    def test_no_cycle_multiple_nodes(self):
        """[1,2,3,4,5], pos=-1 -> None"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                head, _ = build_cycle_list([1, 2, 3, 4, 5], -1)
                self.assertIsNone(sol.detectCycle(head))
