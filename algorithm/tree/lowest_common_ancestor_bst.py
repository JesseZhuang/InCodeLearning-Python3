'''leet code 235 medium'''

from algorithm.struct.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''63ms, 21.02MB'''
        cur = root
        while True:
            if p.val > cur.val and q.val > cur.val: cur=cur.right
            elif p.val<cur.val and q.val<cur.val: cur=cur.left
            else: break
        return cur
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''76ms, 20.76Mb'''
        cur=root
        while (p.val-cur.val)*(q.val-cur.val) > 0:
            cur = cur.left if p.val<cur.val else cur.right
        return cur
