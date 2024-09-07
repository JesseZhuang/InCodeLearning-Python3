"""leet code """
from typing import (
    List,
)


# You can use read4() function by self.read4()
class Solution:
    """
    @param buf: destination
    @param n: the number of characters that need to be read
    @return: the number of characters read
    """

    def read(self, buf: List[str], n: int) -> int:
        buf4 = [0 for i in range(4)]
        v, cnt = 4, 0
        while v >= 4:
            v = self.read4(buf4)
            for i in range(v):
                buf[cnt] = buf4[i]
                cnt += 1
            if cnt >= n: return n
        return cnt

    def read4(self, buf4):
        return 1
