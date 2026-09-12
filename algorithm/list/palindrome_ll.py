"""leet code 234, easy, tags: linked list, two pointers, stack, recursion."""
from typing import Optional

from algorithm.jzstruct.list_node import ListNode


class Solution:
    """O(n) time, O(1) space. Reverse first half in-place, compare, restore."""

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev, slow, fast = None, head, head
        while fast and fast.next:  # O(n/2)
            fast = fast.next.next
            temp = rev
            rev = slow
            slow = slow.next
            rev.next = temp
        tail = slow.next if fast else slow  # odd: skip middle
        while rev:  # O(n/2)
            if rev.val != tail.val: return False
            tail = tail.next
            temp = rev
            rev = rev.next
            temp.next = slow
            slow = temp
        return True


class Solution2:
    """O(n) time, O(n) space. Collect first half with stack, compare with second half."""

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        stack = []
        while fast and fast.next:  # O(n/2)
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:  # odd number of nodes, skip middle
            slow = slow.next
        while slow:  # O(n/2)
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        return True
