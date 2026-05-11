"""LeetCode 143, medium, tags: linked list, two pointers, stack, recursion."""
from typing import Optional

from algorithm.jzstruct.list_node import ListNode


class Solution:
    """Find middle, reverse second half, merge two halves. O(n) time, O(1) space."""

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # find the middle: slow stops at end of first half
        slow, fast = head, head
        while fast.next and fast.next.next:  # O(n/2)
            slow = slow.next
            fast = fast.next.next
        # reverse second half
        prev, cur = None, slow.next  # O(n/2)
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # merge two halves: head and prev
        first, second = head, prev
        while second:  # O(n/2)
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


class Solution2:
    """Stack-based: push all nodes, then weave. O(n) time, O(n) space."""

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        stack = []
        cur = head
        while cur:  # O(n)
            stack.append(cur)
            cur = cur.next
        n = len(stack)
        cur = head
        for i in range(n // 2):  # O(n/2)
            tail = stack.pop()
            tail.next = cur.next
            cur.next = tail
            cur = tail.next
        cur.next = None
