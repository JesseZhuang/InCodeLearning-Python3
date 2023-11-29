'''leet code 1249 medium'''

from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''90ms, 18.30MB'''
        left, right, l = 0, 0, len(s)
        for c in s:
            if c == ')': right += 1
        res = []
        for c in s:
            if c == '(':
                if left == right: continue
                left += 1
            elif c == ')':
                right -=1
                if left == 0: continue
                left -=1
            res.append(c)
        return ''.join(res)
    
    def minRemoveToMakeValid(self, s: str) -> str:
        '''79ms, 18.2MB'''
        sa = list(s)
        stack = deque()
        for i,c in enumerate(sa):
            if c=='(': stack.append(i)  # note: not push()
            elif c==')':
                if len(stack)>0: stack.pop()
                else: sa[i]=''
        while len(stack)>0: sa[stack.pop()]=''
        return ''.join(sa)
    