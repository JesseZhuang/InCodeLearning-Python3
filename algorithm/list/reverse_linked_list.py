"""leet code 206, easy"""
from typing import Optional

from algorithm.jzstruct.list_node import ListNode


class Solution1:
    """0 ms, 18.58 mb"""

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        while head:  # revise head.next (tmp to res), advance res and head
            tmp = head.next
            head.next = res
            res = head
            head = tmp  # head point to None at the end
        return res


class Solution2:
    """0 ms, 18.77 mb"""

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        res = self.reverseList(head.next)  # get the new head, then reverse the last two links
        head.next.next = head  # reverse head.next.next
        head.next = None  # reverse head.next
        return res
