"""leet code 25, hard"""
from typing import Optional

from algorithm.jzstruct.list_node import ListNode


class Solution1:
    """Iterative approach. O(n) time, O(1) space."""

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self._get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # reverse the group
            prev, cur = group_next, group_prev.next  # O(k) per group
            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            # connect with previous part
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def _get_kth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur


class Solution2:
    """Recursive approach. O(n) time, O(n/k) space for recursion stack."""

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur and count < k:  # O(k) check if k nodes exist
            cur = cur.next
            count += 1
        if count < k:
            return head

        # reverse first k nodes
        prev, cur = None, head  # O(k)
        for _ in range(k):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # head is now the tail of the reversed group
        head.next = self.reverseKGroup(cur, k)  # O(n/k) recursion depth
        return prev
