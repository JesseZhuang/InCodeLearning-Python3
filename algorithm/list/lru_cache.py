"""leet 146, lint 134, medium"""


def delete(node):
    node.pre.nex = node.nex
    node.nex.pre = node.pre


class LRUCache:
    """118 ms, 77.4 mb"""

    def __init__(self, capacity: int):
        self.head, self.tail = Node(), Node()
        self.head.nex = self.tail
        self.tail.prev = self.head
        self.kn = dict()
        self.cnt = 0
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.kn:
            self.move_front(self.kn[key])
            return self.kn[key].v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kn:
            self.kn[key].v = value
            self.move_front(self.kn[key])
        else:
            node = Node(k=key, v=value)
            self.add_front(node)
            self.cnt += 1
            self.kn[key] = node
            if self.cnt > self.cap:
                tmp = self.pop_tail()
                del self.kn[tmp.k]
                self.cnt -= 1

    def pop_tail(self):
        tmp = self.tail.pre
        delete(tmp)
        return tmp

    def add_front(self, node):
        self.head.nex.pre = node
        node.nex = self.head.nex
        node.pre = self.head
        self.head.nex = node

    def move_front(self, node):
        delete(node)
        self.add_front(node)


class Node:
    def __init__(self, k=0, v=0, pre=None, nex=None):
        self.k = k
        self.v = v
        self.pre = pre
        self.nex = nex
