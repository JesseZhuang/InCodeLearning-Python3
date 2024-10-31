"""leet code 641, medium"""

from algorithm.struct.d_node import DNode


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = DNode(-1)
        self.tail = DNode(-1)
        self.head.prev = self.tail
        self.tail.next = self.head
        self.cap = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.size += 1
        n = DNode(value, prev=self.head.prev, next=self.head)
        self.head.prev.next = n
        self.head.prev = n
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.size += 1
        n = DNode(value, prev=self.tail, next=self.tail.next)
        self.tail.next.prev = n
        self.tail.next = n
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.size -= 1
        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.size -= 1
        self.tail.next.next.prev = self.tail
        self.tail.next = self.tail.next.next
        return True

    def getFront(self) -> int:
        return self.head.prev.v

    def getRear(self) -> int:
        return self.tail.next.v

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap
