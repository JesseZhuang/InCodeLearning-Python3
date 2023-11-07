'''leet code 242, easy'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''55ms, 16.76Mb'''
        if len(s) != len(t):
            return False;
        char_ind = dict()
        for i in range(len(s)):
            char_ind[s[i]] = char_ind.get(s[i],0)+1
            char_ind[t[i]] = char_ind.get(t[i],0)-1
        for v in char_ind.values():
            if v != 0:
                return False
        return True
    

    def isAnagram(self, s: str, t: str) -> bool:
        '''60ms, 16.83Mb'''
        if len(s)!= len(t):
            return False
        count = [0]*26
        a = ord('a')
        for i in range(len(s)):
            count[ord(s[i])-a] += 1
            count[ord(t[i])-a] -= 1
        for c in count:
            if c != 0:
                return False
        return True
