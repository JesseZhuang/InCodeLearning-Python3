'''leet code 91 medium'''


class Solution:
    def numDecodings(self, s: str) -> int:
        cur, prev = 1, 0
        for i in range(len(s)-1, -1, -1):
            ways = 0 if s[i] == '0' else cur
            if i < len(s)-1 and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                ways += prev
            prev = cur
            cur = ways
        return cur
