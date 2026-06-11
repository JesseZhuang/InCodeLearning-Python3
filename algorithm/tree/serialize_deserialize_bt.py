"""LeetCode 297 hard, tags: string, tree, binary tree, design, dfs, bfs."""

from collections import deque

from algorithm.jzstruct.tree_node import TreeNode


class Codec:
    """Preorder DFS serialization. O(n) time, O(n) space."""

    def serialize(self, root: 'TreeNode') -> str:
        tokens = []
        self._ser_helper(root, tokens)
        return ','.join(tokens)

    def _ser_helper(self, node, tokens):
        if node is None:
            tokens.append('#')
        else:
            tokens.append(str(node.val))  # O(1)
            self._ser_helper(node.left, tokens)  # O(left subtree)
            self._ser_helper(node.right, tokens)  # O(right subtree)

    def deserialize(self, data: str) -> 'TreeNode':
        tokens = iter(data.split(','))
        return self._deser_helper(tokens)

    def _deser_helper(self, tokens):
        val = next(tokens)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = self._deser_helper(tokens)
        node.right = self._deser_helper(tokens)
        return node


class Codec2:
    """BFS level-order serialization. O(n) time, O(n) space."""

    def serialize(self, root: 'TreeNode') -> str:
        if not root:
            return ''
        tokens = []
        queue = deque([root])
        while queue:
            node = queue.popleft()  # O(1) amortized
            if node:
                tokens.append(str(node.val))
                queue.append(node.left)  # O(1)
                queue.append(node.right)
            else:
                tokens.append('#')
        return ','.join(tokens)

    def deserialize(self, data: str) -> 'TreeNode':
        if not data:
            return None
        tokens = data.split(',')
        root = TreeNode(int(tokens[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if tokens[i] != '#':
                node.left = TreeNode(int(tokens[i]))
                queue.append(node.left)
            i += 1
            if tokens[i] != '#':
                node.right = TreeNode(int(tokens[i]))
                queue.append(node.right)
            i += 1
        return root
