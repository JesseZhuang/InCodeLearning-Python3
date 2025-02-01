"""leet 1166, lint 3677 medium"""


class Trie:
    def __init__(self, v: int = -1):
        self.next = dict()
        self.v = v

    def insert(self, w: str, v: int) -> bool:
        node = self
        ps = w.split("/")
        for p in ps[1:-1]:
            if p not in node.next:
                return False
            node = node.next[p]
        if ps[-1] in node.next:
            return False
        node.next[ps[-1]] = Trie(v)
        return True

    def search(self, w: str) -> int:
        node = self
        for p in w.split("/")[1:]:
            if p not in node.next:
                return -1
            node = node.next[p]
        return node.v


class FileSystem:
    """lint 162 ms, 5.55 mb"""

    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, value: int) -> bool:
        return self.trie.insert(path, value)

    def get(self, path: str) -> int:
        return self.trie.search(path)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
