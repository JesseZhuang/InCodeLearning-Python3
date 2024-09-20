"""leet code 232, easy"""
from collections import deque


class MyQueue:

    def __init__(self):
        self.input = deque()
        self.out = deque()

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.transfer()
        return self.out.pop()

    def peek(self) -> int:
        self.transfer()
        return self.out[-1]

    def transfer(self):
        if len(self.out) == 0:
            while len(self.input) != 0:
                self.out.append(self.input.pop())

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.out) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
