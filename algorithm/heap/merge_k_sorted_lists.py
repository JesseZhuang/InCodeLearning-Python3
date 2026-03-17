from heapq import heappush, heappop
from typing import List, Optional

from jzstruct.list_node import ListNode


class Solution:
    """7 ms, 20.4 mb"""

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq, dummy = list(), ListNode()
        cur = dummy
        for l in lists:
            if l:
                heappush(pq, (l.val, id(l), l))
        while pq:
            _, _, n = heappop(pq)
            cur.next = n
            n = n.next
            if n:
                heappush(pq, (n.val, id(n), n))
            cur = cur.next
        return dummy.next
