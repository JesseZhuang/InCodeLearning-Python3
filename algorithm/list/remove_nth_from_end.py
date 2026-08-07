"""LeetCode 19, medium, tags: linked list, two pointers."""
from typing import Optional

from algorithm.jzstruct.list_node import ListNode


class Solution:
    """Two pointers with n-gap. O(n) time, O(1) space."""

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        front, back = dummy, dummy
        for _ in range(n + 1):  # O(n) advance front n+1 steps
            front = front.next
        while front:  # O(n) advance both until front reaches end
            front = front.next
            back = back.next
        back.next = back.next.next  # O(1) remove the nth node from end
        return dummy.next


class Solution2:
    """Single pass counting. O(n) time, O(1) space."""

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur, nth = head, dummy
        count = 0
        while cur:  # O(n)
            cur = cur.next
            count += 1
            if count > n:
                nth = nth.next
        nth.next = nth.next.next
        return dummy.next
