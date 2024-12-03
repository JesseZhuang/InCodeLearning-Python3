"""
platform: hackerrank
companies: goldman sachs, salesforce, vmware
related to leet 91 lint 512, medium
"""


def convert(s: str) -> str:
    return chr(int(s))


def decode_ascii_string(s: str) -> str:
    s, i, res = s[::-1], 0, []
    while i < len(s):
        if '3' <= s[i] <= '9':
            res.append(convert(s[i:i + 2]))
            i += 2
        else:
            res.append(convert(s[i:i + 3]))
            i += 3
    return ''.join(res)


def decode_ascii_string_dp(s: str) -> list[str]:
    s, n = s[::-1], len(s)
    dp, dp1, dp2, dp3 = [], [], [''], []  # dp, dp[i+1], dp[i+2], dp[i+3]
    for i in range(n - 2, -1, -1):
        dp = [] if s[i] == '0' else [convert(s[i:i + 2]) + s1 for s1 in dp2]
        if i < n - 2 and '10' <= s[i:i + 2] <= '12' and s[i:i + 3] <= '126':
            dp += [convert(s[i:i + 3]) + s1 for s1 in dp3]
        dp3 = dp2
        dp2 = dp1
        dp1 = dp
    return dp


def encode_ascii_string(s: str) -> str:
    return ''.join(map(str, map(ord, s)))[::-1]
