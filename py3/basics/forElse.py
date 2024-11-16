# usage of for else
# else will only break out the first for loop, different java, c
# use Eratosthenes sieve to find prime numbers in [1, 100]

from math import sqrt

for n in range(1, 100):
    t = int(sqrt(n))
    for m in range(2, t + 1):
        if n % m == 0:
            break
    else:
        print(n)
