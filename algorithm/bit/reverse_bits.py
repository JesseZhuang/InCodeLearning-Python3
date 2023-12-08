'''leet code 190 easy'''


class Solution:
    def reverseBits(self, n: int) -> int:
        '''40ms, 16.29Mb'''
        res = 0
        for i in range(32):
            res <<= 1
            res += n & 1
            n >>= 1
        return res

    def reverseBits(self, n: int) -> int:
        '''44ms, 16.4Mb'''
        n = (n >> 16) | (n << 16)
        n = ((n >> 8) & 0x00ff00ff) | ((n << 8) & 0xff00ff00)
        n = ((n >> 4) & 0x0f0f0f0f) | ((n << 4) & 0xf0f0f0f0)
        n = ((n >> 2) & 0x33333333) | ((n << 2) & 0xcccccccc)
        n = ((n >> 1) & 0x55555555) | ((n << 1) & 0xaaaaaaaa)
        return n
