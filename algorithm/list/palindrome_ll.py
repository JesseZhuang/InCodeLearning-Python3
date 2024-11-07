"""leet code 234, easy"""
from typing import Optional

from algorithm.struct.list_node import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            temp = rev  # save rev
            rev = slow  # advance rev
            slow = slow.next  # advance slow
            rev.next = temp  # reverse
        tail = slow.next if fast else slow
        while rev:
            if rev.val != tail.val: return False
            tail = tail.next
            temp = rev  # save rev
            rev = rev.next  # advance rev
            temp.next = slow  # reverse
            slow = temp  # advance slow
        return True
