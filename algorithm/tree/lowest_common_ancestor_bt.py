"""LeetCode 236, medium, tags: tree, dfs, binary tree."""
from algorithm.jzstruct.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Recursive DFS. O(n) time, O(h) space."""
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Iterative with parent pointers. O(n) time, O(n) space."""
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:  # O(n)
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:  # O(h)
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:  # O(h)
            q = parent[q]
        return q
