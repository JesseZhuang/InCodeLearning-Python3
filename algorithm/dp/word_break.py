'''leet code 139, medium'''

from collections import deque
from typing import List


class Solution:
    def wordBreakBFS(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        visited = [False]*l
        q = deque()
        q.append(0)
        w_d = set(wordDict)
        while len(q) > 0:
            start = q.popleft()
            if visited[start]:
                continue
            for end in range(start+1, l+1):
                if s[start:end] in w_d:
                    q.append(end)
                    if end == l:
                        return True
            visited[start] = True
        return False
