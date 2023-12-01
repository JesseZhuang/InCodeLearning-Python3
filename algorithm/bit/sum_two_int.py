'''leet code 371 medium'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0 or b == 0: return a|b
        mask = 0xffffffff
        while b&mask > 0:
            carry = a&b
            a ^= b
            b = carry << 1
        return a if b == 0 else a&mask  # return a&mask if b overflow
        # return a&mask fails for -12 + -8, expected -20, actual 4294967276
        # return a fails for -1 + 1, expected 0, actual -4294967296
