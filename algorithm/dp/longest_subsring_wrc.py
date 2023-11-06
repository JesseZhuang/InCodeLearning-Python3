'''leet code 3 medium'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''67ms, 16.2Mb'''
        res = 0
        char_ind = dict()
        l,r = 0,0
        while r < len(s):
            if s[r] in char_ind:
                l = max(l, char_ind[s[r]]+1)
            char_ind[s[r]] = r
            res = max(res, r-l+1)
            r += 1
        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        '''64ms, 16.29Mb'''
        res, l, r = 0,0,0
        char_ind = [None] * 128
        for c in s:
            i = ord(c)
            if char_ind[i] != None:  # 0 considered false
                l = max(l, char_ind[i]+1)
            char_ind[i] = r
            res = max(res, r-l+1)
            r += 1
        return res
