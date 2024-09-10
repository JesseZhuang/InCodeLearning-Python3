"""lint code 300, medium"""
import collections

# Example 1
#
# Input:
# meeting = [[10,40],[20,50],[30,45],[40,60]]
# value = [3,6,2,4]
# Output: 7
# Explanation: You can take the 0th meeting and the 3th meeting, you can get 3 + 4 = 7.
# Example 2
#
# Input:
# meeting = [[10,20],[20,30]]
# value = [2,4]
# Output: 6
# Explanation: You can take the 0th meeting and the 1st

# 0≤len(meeting)=len(value)≤10000
# 1≤meeting[i][0]<meeting[i][1]≤50000
# value_i≤10000
# (0,8),(8,10) is not conflict at 8

MAX_TIME = 50000


class Solution:

    def maxValue(self, meetings, values):
        """
        @param meeting: the meetings
        @param value: the value
        @return: calculate the max value
        """
        end_start_val = collections.defaultdict(list)
        for i in range(len(meetings)):
            end_start_val[meetings[i][1]].append((meetings[i][0], values[i]))

        dp = [0] * (MAX_TIME + 1)
        for i in range(1, MAX_TIME + 1):
            dp[i] = dp[i - 1]  # do not attend any meetings
            for start, value in end_start_val[i]:
                dp[i] = max(dp[i], dp[start] + value)  # pick max val meeting to attend
        return max(dp)
