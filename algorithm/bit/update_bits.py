"""lint code 179, medium"""

from ctypes import c_int32


class Solution:

    def updateBits(self, n, m, i, j):  # 456, 31, 27, 31
        mask = (1 << i) - 1 if j == 31 else ~((1 << j + 1) - (1 << i))
        res = n & mask | m << i  # hex(4160750024) '0xf800_01c8'
        if res & (1 << 31):  # sign bit
            res = c_int32(res).value  # hex(-134217272) '-0x7ff_fe38', in java, still 0xf800_01c8
        return res
