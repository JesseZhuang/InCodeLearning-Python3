"""leet code 2130, medium — Maximum Twin Sum of a Linked List"""
from typing import Optional

from algorithm.jzstruct.list_node import ListNode


class Solution:
    def pair_sum(self, head: Optional[ListNode]) -> int:
        """Reverse second half approach.
        Time:  O(n) — three passes: find middle, reverse, traverse
        Space: O(1) — only pointer manipulation, no extra storage
        """
        slow, fast = head, head
        while fast and fast.next:  # O(n/2) find middle
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:  # O(n/2) reverse second half
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        max_sum = 0
        left, right = head, prev
        while right:  # O(n/2) pair up twins
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next
        return max_sum

    def pair_sum_stack(self, head: Optional[ListNode]) -> int:
        """Stack approach — push first half, pop to pair with second half.
        Time:  O(n) — two passes: push first half, pair second half
        Space: O(n) — stack stores n/2 elements
        """
        slow, fast = head, head
        stack = []
        while fast and fast.next:  # O(n/2)
            stack.append(slow.val)  # O(n/2) space for stack
            slow = slow.next
            fast = fast.next.next

        max_sum = 0
        while slow:  # O(n/2) pair with popped values
            max_sum = max(max_sum, stack.pop() + slow.val)
            slow = slow.next
        return max_sum
