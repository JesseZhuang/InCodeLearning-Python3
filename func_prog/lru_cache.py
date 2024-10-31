"""functools.lru_cache"""

import functools
import sys
import time


def fib_no_cache(n: int) -> int:
    """fibonacci without cache"""
    if n < 2:
        return n
    return fib_no_cache(n - 1) + fib_no_cache(n - 2)


@functools.lru_cache(maxsize=None)
def fib_lru_cache(n: int) -> int:
    """with lru cache, no size limit"""
    if n < 2:
        return n
    return fib_lru_cache(n - 1) + fib_lru_cache(n - 2)


print(sys.getrecursionlimit())  # 1000
sys.setrecursionlimit(1100)

begin = time.time()
fib_no_cache(35)
end = time.time()

print("Time taken to execute the\
function without lru_cache is", end - begin)

begin = time.time()
fib_lru_cache(35)
end = time.time()

print("Time taken to execute the \
function with lru_cache is", end - begin)

# example output for n = 35
# Time taken to execute the function without lru_cache is 3.162417411804199
# Time taken to execute the function with lru_cache is 3.0040740966796875e-05
