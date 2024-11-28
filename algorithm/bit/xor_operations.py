"""hackerrank, salesforce, medium"""


def xor_operations(arr: list[int], k: int) -> list[int]:
    """k,1"""
    n = len(arr)
    for i in range(k):
        arr[i % n] ^= arr[n - (i % n) - 1]
    return arr


def xor_operations_1(arr: list[int], k: int) -> list[int]:
    """n,1"""
    n = len(arr)
    if n % 2 == 1:
        arr[n // 2] = 0 if k > n // 2 else arr[n // 2]
    k %= n * 3  # k in [0,3n-1]
    for i in range(n // 2):
        a, b = arr[i], arr[n - 1 - i]
        xor = a ^ b
        arr[i] = [xor, b, a][(k - 1 - i) // n]  # (k+n-1-i)//n-1, map k in [1,n]->0
        arr[n - 1 - i] = [b, a, xor][(k + i) // n]  # (k+n+i)//n-1, map k in [0,n-1]->0
    return arr
