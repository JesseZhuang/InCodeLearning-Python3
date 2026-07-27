"""LeetCode 148, medium, tags: linked list, two pointers, divide and conquer, sorting, merge sort."""
from typing import Optional

from algorithm.jzstruct.list_node import ListNode


class Solution:
    """Bottom-up merge sort. O(n log n) time, O(1) space."""

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = 0
        cur = head
        while cur:  # O(n) count length
            n += 1
            cur = cur.next
        dummy = ListNode(0)
        dummy.next = head
        step = 1
        while step < n:  # O(log n) passes
            prev, cur = dummy, dummy.next
            while cur:  # O(n) per pass
                left = cur
                right = self._split(left, step)
                cur = self._split(right, step)
                prev = self._merge(left, right, prev)
            step <<= 1
        return dummy.next

    def _split(self, head: Optional[ListNode], step: int) -> Optional[ListNode]:
        if not head:
            return None
        for _ in range(step - 1):  # advance step-1 nodes
            if not head.next:
                break
            head = head.next
        right = head.next
        head.next = None
        return right

    def _merge(self, left: Optional[ListNode], right: Optional[ListNode],
               prev: ListNode) -> ListNode:
        cur = prev
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left if left else right
        while cur.next:  # advance to tail
            cur = cur.next
        return cur


class Solution2:
    """Top-down merge sort (recursive). O(n log n) time, O(log n) space for recursion stack."""

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:  # O(n/2) find middle
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)  # T(n/2)
        right = self.sortList(mid)  # T(n/2)
        return self._merge(left, right)

    def _merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:  # O(n)
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next
