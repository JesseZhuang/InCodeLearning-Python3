import unittest

from algorithm.list.copy_list_with_random_pointer import Node, Solution, Solution2


def build(vals_and_randoms):
    """Build linked list from list of [val, random_index]. random_index can be None."""
    if not vals_and_randoms:
        return None
    nodes = [Node(v) for v, _ in vals_and_randoms]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, r) in enumerate(vals_and_randoms):
        if r is not None:
            nodes[i].random = nodes[r]
    return nodes[0]


def to_list(head):
    """Convert linked list to list of [val, random_index] for verification."""
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    node_to_idx = {id(n): i for i, n in enumerate(nodes)}
    return [[n.val, node_to_idx.get(id(n.random))] for n in nodes]


class TestCopyListWithRandomPointer(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, vals_and_randoms):
        for sol in self.solutions:
            head = build(vals_and_randoms)
            copied = sol.copyRandomList(head)
            result = to_list(copied) if copied else []
            expected = [[v, r] for v, r in vals_and_randoms] if vals_and_randoms else []
            self.assertEqual(expected, result, f"{sol.__class__.__name__}")
            if head:
                cur_orig, cur_copy = head, copied
                while cur_orig:
                    self.assertIsNot(cur_orig, cur_copy)
                    cur_orig = cur_orig.next
                    cur_copy = cur_copy.next

    def test_example1(self):
        self.verify([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])

    def test_example2(self):
        self.verify([[1, 1], [2, 1]])

    def test_example3(self):
        self.verify([[3, None], [3, 0], [3, None]])

    def test_empty(self):
        self.verify([])

    def test_single_no_random(self):
        self.verify([[1, None]])

    def test_single_self_random(self):
        self.verify([[1, 0]])

    def test_all_random_to_self(self):
        self.verify([[1, 0], [2, 1], [3, 2]])

    def test_all_random_to_last(self):
        self.verify([[1, 2], [2, 2], [3, None]])

    def test_large_values(self):
        self.verify([[-10000, 1], [10000, 0]])


if __name__ == '__main__':
    unittest.main()
