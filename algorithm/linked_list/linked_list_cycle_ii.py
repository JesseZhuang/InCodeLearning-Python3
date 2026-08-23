"""LeetCode 142, medium — Linked List Cycle II"""
from typing import Optional

from algorithm.jzstruct.list_node import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Floyd's tortoise and hare algorithm.
        Time:  O(n) — at most 2 passes through the list
        Space: O(1) — two pointers only
        """
        slow = fast = head
        while fast and fast.next:  # O(n)
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:  # O(n) find cycle start
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


class Solution2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """HashSet approach.
        Time:  O(n) — single pass
        Space: O(n) — store visited nodes
        """
        seen = set()
        cur = head
        while cur:  # O(n)
            if cur in seen:
                return cur
            seen.add(cur)
            cur = cur.next
        return None
