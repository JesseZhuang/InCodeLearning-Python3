"""
find all occurrences of the pattern inside the text.
O(n) time, O(1) space not considering result Z array.

For a string str[0..n-1], Z array is of same length as string. An element Z[i] of Z array stores length of the longest
 substring starting from str[i] which is also a prefix of str[0..n-1]. The first entry of Z
 array is meaning less as complete string is always prefix of itself.
"""
from typing import List


def zfunc(s: str) -> List[int]:
    n = len(s)
    Z = [0] * n
    l = r = 0
    for i in range(n):
        if r > l: Z[i] = min(r - i, Z[i - l])
        while i + Z[i] < n and s[i] == s[i + Z[i]]: Z[i] += 1
        if i + Z[i] > r:
            r = i + Z[i]
            l = i
    return Z
