from collections import defaultdict


class FreqStack:
    """LeetCode 895, hard, tags: hash table, stack, design, ordered set.

    Design a stack-like data structure to push elements to the stack and pop the most frequent element.

    Implement the FreqStack class:
    - FreqStack() constructs an empty frequency stack.
    - void push(int val) pushes an integer val onto the top of the stack.
    - int pop() removes and returns the most frequent element in the stack.
      If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

    Constraints:
    - 0 <= val <= 10^9
    - At most 2 * 10^4 calls total will be made to push and pop.
    - It is guaranteed that there will be at least one element in the stack before calling pop.
    """

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)  # O(n) space, freq -> stack of vals
        self.max_freq = 0

    def push(self, val: int) -> None:  # O(1) time
        self.freq[val] += 1
        f = self.freq[val]
        if f > self.max_freq:
            self.max_freq = f
        self.group[f].append(val)

    def pop(self) -> int:  # O(1) time
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
