"""LeetCode 117: populate each node's next pointer to its next right node."""

from collections import deque
from typing import Optional


class Node:
    """Binary tree node with the additional next-level pointer."""

    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        """Link nodes level by level with a queue: O(n) time, O(w) space."""
        if root is None:
            return None

        root.next = None
        queue = deque([root])
        while queue:
            previous = None
            # Every node enters and leaves the queue once: O(n) total time.
            for _ in range(len(queue)):
                node = queue.popleft()
                if previous is not None:
                    previous.next = node
                previous = node
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            # The rightmost node on this level must not point into another level.
            previous.next = None

        return root

    def connectConstantSpace(self, root: Optional[Node]) -> Optional[Node]:
        """Build each level's links while walking the previous one: O(n)/O(1)."""
        if root is None:
            return None

        root.next = None
        level = root
        while level is not None:
            next_head = None
            next_tail = None
            node = level
            # Each existing node is visited once; only a fixed number of pointers
            # are used beyond the input tree, so total work is O(n) and extra space O(1).
            while node is not None:
                for child in (node.left, node.right):
                    if child is not None:
                        if next_tail is None:
                            next_head = child
                        else:
                            next_tail.next = child
                        next_tail = child
                node = node.next

            if next_tail is not None:
                next_tail.next = None
            level = next_head

        return root
