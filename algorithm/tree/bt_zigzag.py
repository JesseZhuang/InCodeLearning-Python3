"""leet code 103, medium"""
from collections import deque
from typing import Optional, List

from algorithm.struct.tree_node import TreeNode


class Solution3:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = deque([root]) if root else None
        odd = False  # root level 0, even level
        while q:
            n, cur = len(q), deque()
            for _ in range(n):
                node = q.popleft()
                if odd:
                    cur.appendleft(node.val)
                else:
                    cur.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(list(cur))  # O(n) unfortunately python does not have linkedlist
            odd = not odd
        return res


class Solution1:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = list()
        q, even = deque([root]) if root else None, True  # even level, starting with level 0

        def add():
            n = q.popleft() if even else q.pop()
            cur.append(n.val)
            children = [n.left, n.right] if even else [n.right, n.left]
            for c in children:
                if c:
                    q.append(c) if even else q.appendleft(c)

        while q:
            n, cur = len(q), list()
            for _ in range(n):
                add()
            even = not even
            res.append(cur)
        return res


class Solution2:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(n: Optional[TreeNode], h: int):
            if not n: return
            if len(res) <= h: res.append([])
            res[h].append(n.val)
            dfs(n.left, h + 1)
            dfs(n.right, h + 1)

        dfs(root, 0)
        # reverse takes extra time
        return [res[i] if i & 1 == 0 else res[i][::-1] for i in range(len(res))]
