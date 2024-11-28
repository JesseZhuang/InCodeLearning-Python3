"""hacker rank, salesforce, easy"""


def better_compression(s: str) -> str:
    """n,26"""
    n, res, i = len(s), [0] * 26, 0
    while i < n:
        c, cnt = s[i], 0
        i += 1
        while i < n and s[i].isdigit():
            cnt = cnt * 10 + int(s[i])
            i += 1
        res[ord(c) - ord('a')] += cnt
    return ''.join(chr(i + ord('a')) + str(res[i]) for i in range(26) if res[i])
