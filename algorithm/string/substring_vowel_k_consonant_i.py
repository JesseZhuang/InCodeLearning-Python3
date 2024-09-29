"""
leet code weekly 417, Q2, medium
return total number of substrings that contains every vowel at least once and exactly k consonants.

Constraints:
1. 5 <= word.length <= 250, n
2. word consists only of lowercase English letters.
3. 0 <= k <= word.length - 5
"""
from collections import Counter


class Solution:
    """n^2, 1, Yawn_Sean"""

    def countOfSubstrings(self, s: str, k: int) -> int:
        vow = set('aeiou')
        n = len(s)

        def solve(k):
            """result for at least k consonants and 5 vowels at least once"""
            l, r = 0, 0
            cnt = Counter()  # seen vowels
            cur1 = cur2 = 0  # unique vowels seen, consonants seen
            res = 0
            while l < n:
                while r < n and (cur1 < 5 or cur2 < k):
                    if s[r] in vow:
                        if cnt[s[r]] == 0: cur1 += 1
                        cnt[s[r]] += 1
                    else:
                        cur2 += 1
                    r += 1
                if cur1 < 5 or cur2 < k: break  # not possible
                res += n + 1 - r  # important do not have to increment res 1by1
                if s[l] in vow:
                    cnt[s[l]] -= 1
                    if cnt[s[l]] == 0: cur1 -= 1
                else:
                    cur2 -= 1
                l += 1
            return res

        return solve(k) - solve(k + 1)
