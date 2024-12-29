"""leet 2471, medium"""
from collections import deque
from typing import Optional

from jzstruct.tree_node import TreeNode


class Solution:
    """todo editorial"""
    # Constants for bit manipulation
    _SHIFT = 20
    _MASK = 0xFFFFF

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        swaps = 0

        # Process tree level by level using BFS
        while queue:
            level_size = len(queue)
            nodes = []

            # Store node values with encoded positions
            for i in range(level_size):
                node = queue.popleft()
                # Encode value and index: high 20 bits = value, low 20 bits = index
                nodes.append((node.val << self._SHIFT) + i)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Sort nodes by their values (high 20 bits)
            nodes.sort()

            # Count swaps needed to match indices with original positions
            i = 0
            while i < level_size:
                orig_pos = nodes[i] & self._MASK
                if orig_pos != i:
                    # Swap nodes and decrement i to recheck current position
                    nodes[i], nodes[orig_pos] = nodes[orig_pos], nodes[i]
                    swaps += 1
                    i -= 1
                i += 1

        return swaps
