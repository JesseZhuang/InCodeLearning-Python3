"""leet code 2, medium — Add Two Numbers"""
from typing import Optional

from algorithm.jzstruct.list_node import ListNode


class Solution:
    def add_two_numbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Iterative approach using dummy head.
        Time:  O(max(m, n)) — iterate both lists once
        Space: O(max(m, n)) — new list stores the result
        """
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:  # O(max(m,n)) iterate both lists
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
        return dummy.next

    def add_two_numbers_recursive(
        self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0
    ) -> Optional[ListNode]:
        """Recursive approach — same complexity, different structure.
        Time:  O(max(m, n)) — one recursive call per digit
        Space: O(max(m, n)) — recursion stack + result list
        """
        if not l1 and not l2 and not carry:
            return None
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        node = ListNode(total % 10)  # O(max(m,n)) space for result nodes
        node.next = self.add_two_numbers_recursive(l1, l2, total // 10)
        return node
