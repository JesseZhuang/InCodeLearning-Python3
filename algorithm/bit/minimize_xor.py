"""leet 2429, medium"""


class Solution:
    """todo editorial"""

    def minimizeXor(self, num1, num2):
        a, b = num1.bit_count(), num2.bit_count()
        res = num1
        for i in range(32):
            if a > b and (1 << i) & num1 > 0:
                res ^= 1 << i
                a -= 1
            if a < b and (1 << i) & num1 == 0:
                res ^= 1 << i
                a += 1
        return res
