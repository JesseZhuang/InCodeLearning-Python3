"""leet code 432, hard"""


class Node:
    def __init__(self, cnt=-1, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.cnt = cnt
        self.keys = set()
        if prev: prev.next = self
        if next: next.prev = self


class AllOne:
    """67ms, 33.46mb"""

    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.key_node = dict()

    def inc(self, key: str) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            node.keys.remove(key)
            self.updateNode(node.cnt + 1, key, node, True)
            if not node.keys: AllOne.removeNode(node)
        else:
            self.updateNode(1, key, self.head, True)

    def dec(self, key: str) -> None:
        if key not in self.key_node: return
        node = self.key_node[key]
        node.keys.remove(key)
        cnt = node.cnt
        if cnt == 1:
            del self.key_node[key]
        else:
            self.updateNode(cnt - 1, key, node, False)
        if not node.keys: AllOne.removeNode(node)

    def getMaxKey(self) -> str:
        if self.head.next == self.tail: return ''
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail: return ''
        return next(iter(self.head.next.keys))

    @staticmethod
    def removeNode(node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def updateNode(self, cnt: int, key: str, node: Node, inc: bool) -> None:
        prev, next = node.prev, node.next
        if inc:
            res = next if next.cnt == cnt else Node(cnt=cnt, prev=node, next=next)
        else:
            res = prev if prev.cnt == cnt else Node(cnt=cnt, prev=prev, next=node)
        res.keys.add(key)
        self.key_node[key] = res
