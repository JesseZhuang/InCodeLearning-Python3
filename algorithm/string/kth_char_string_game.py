"""
leet code weekly 417, Q1, easy
start with string "a"
operation, change each letter in string to the next, wrap around (z->a) and append it to original string
return kth character in word after enough operations so that word has at least k characters.

Constraints:
1 <= k <= 500
"""


class Solution:
    """k, 1 or k"""

    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            tmp = map(ord, list(s))
            tmp = map(lambda n: n + 1 if n + 1 <= 122 else n + 1 - 26, tmp)
            tmp = map(chr, tmp)
            s += "".join(tmp)
        return s[k - 1]


s = "a"
while len(s) < 500:
    s += ''.join(chr(ord(x) + 1) for x in s)


class Solution2:
    def kthCharacter(self, k: int) -> str:
        return s[k - 1]
