class DNode:
    """doubly linked node"""

    def __init__(self, v: int, prev=None, next=None):  # ok to shadow builtin next
        self.v = v
        self.prev = prev
        self.next = next
