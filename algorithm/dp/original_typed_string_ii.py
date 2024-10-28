"""leet code 3333, hard"""


class Solution:
    """@duhlavya"""

    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        runs = []
        cur_ch = word[0]
        cnt = 1

        for char in word[1:]:
            if char == cur_ch:
                cnt += 1
            else:
                runs.append(cnt)
                cur_ch = char
                cnt = 1
        runs.append(cnt)

        R = len(runs)
        total_ways = 1
        for length in runs:
            total_ways = (total_ways * length) % MOD

        S = k - R - 1
        if S < 0:
            return total_ways

        dp = [0] * (S + 1)  # dp[0,S] res for string size [R, k-1]
        dp[0] = 1

        for length in runs:
            mi = length - 1
            new_dp = [0] * (S + 1)
            prefix_sum = 0
            for j in range(S + 1):
                prefix_sum = (prefix_sum + dp[j]) % MOD
                if j > mi:
                    prefix_sum = (prefix_sum - dp[j - mi - 1] + MOD) % MOD
                new_dp[j] = prefix_sum
            dp = new_dp

        invalid = sum(dp) % MOD
        result = (total_ways - invalid + MOD) % MOD
        return result
