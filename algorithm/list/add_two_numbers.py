"""leet code 2, medium"""
from typing import Optional

from algorithm.jzstruct.list_node import ListNode


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """two pointer"""
    dummy = ListNode()
    cur = dummy
    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        sum += carry
        carry = sum // 10
        sum = sum % 10
        cur.next = ListNode(sum)
        cur = cur.next
    return dummy.next
