"""leet code 158, hard"""

"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""


class Solution:

    def __init__(self):
        self.done = False
        self.i = 0
        self.size = 0
        self.buf4 = [0] * 4

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        j = 0
        while j < n:
            while self.i == self.size:
                if self.done: return j
                self.size = Reader.read4(self.buf4)
                self.i = 0
                if self.size < 4: self.done = True
            while j < n and self.i < self.size:
                buf[j] = self.buf4[self.i]
                j += 1
                self.i += 1
        return j


class Reader:
    def read4(self, buf):
        return 1
