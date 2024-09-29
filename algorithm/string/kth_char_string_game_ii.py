"""
leet code weekly 417, Q4, hard
start with string "a"
If operations[i] == 0, append a copy of word to itself.
If operations[i] == 1, change each letter in string to the next, wrap around (z->a) and append it to original string
return kth character in word after enough operations so that word has at least k characters.

Constraints:
1. 1 <= k <= 10^14
2. 1 <= operations.length <= 100, op should be ceil(lgk)
3. operations[i] is either 0 or 1.
4. The input is generated such that word has at least k characters after all operations.

test cases:
k   operations expected
5   [0,0,0]     "a"
10  [0,1,0,1]   "b"
"""
from typing import List


class Solution:
    """
    op or ceil(lgk)-1, 1
    number of characters in string always double
    ith char will be operated to become 2*i th, then 4*i th
    also, ith -> i+2 th -> i+4 th -> i+8 th ...
    """

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        c = 0
        for i in range(k.bit_length() - 1, -1, -1):
            if k >> i & 1:
                c += operations[i]
        return chr(ord('a') + c % 26)
