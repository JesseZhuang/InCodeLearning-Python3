"""LeetCode 138, medium, tags: hash table, linked list."""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """Hash map approach. O(n) time, O(n) space."""

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        old_to_new = {}
        cur = head
        while cur:  # O(n) first pass: create all copy nodes
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:  # O(n) second pass: wire next and random pointers
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next
        return old_to_new[head]


class Solution2:
    """Interleaving approach. O(n) time, O(1) space."""

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        # O(n) step 1: interleave copies — A -> A' -> B -> B' -> ...
        cur = head
        while cur:
            copy = Node(cur.val, cur.next)
            cur.next = copy
            cur = copy.next
        # O(n) step 2: assign random pointers for copies
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # O(n) step 3: separate the two lists
        dummy = Node(0)
        copy_cur = dummy
        cur = head
        while cur:
            copy_cur.next = cur.next
            copy_cur = copy_cur.next
            cur.next = copy_cur.next
            cur = cur.next
        return dummy.next
