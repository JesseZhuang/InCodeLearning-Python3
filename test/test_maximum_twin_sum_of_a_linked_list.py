import unittest

from algorithm.jzstruct.list_node import ListNode
from algorithm.linked_list.maximum_twin_sum_of_a_linked_list import Solution


def to_linked_list(nums):
    dummy = ListNode()
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next


class TestMaximumTwinSum(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def _run(self, vals, expected):
        for sol in self.solutions:
            for method_name in ("pair_sum", "pair_sum_stack"):
                with self.subTest(method=method_name):
                    head = to_linked_list(vals)
                    result = getattr(sol, method_name)(head)
                    self.assertEqual(result, expected)

    def test_example1(self):
        self._run([5, 4, 2, 1], 6)

    def test_example2(self):
        self._run([4, 2, 2, 3], 7)

    def test_example3(self):
        self._run([1, 100000], 100001)

    def test_two_elements(self):
        self._run([1, 1], 2)

    def test_symmetric(self):
        # twins: (0,3)=1+1=2, (1,2)=2+2=4
        self._run([1, 2, 2, 1], 4)

    def test_all_same(self):
        self._run([5, 5, 5, 5], 10)

    def test_max_at_edges(self):
        self._run([100, 1, 1, 100], 200)

    def test_max_at_center(self):
        # twins: (0,3)=1+1=2, (1,2)=100+100=200
        self._run([1, 100, 100, 1], 200)

    def test_six_elements(self):
        # twins: (0,5)=1+6=7, (1,4)=2+5=7, (2,3)=3+4=7
        self._run([1, 2, 3, 4, 5, 6], 7)

    def test_descending(self):
        # twins: (0,3)=4+1=5, (1,2)=3+2=5
        self._run([4, 3, 2, 1], 5)


if __name__ == "__main__":
    unittest.main()
