"""leet 2054, medium"""


class Solution:
    """todo editorial, greedy, 269 ms, 73.1 mb"""

    def maxTwoEvents(self, events):
        times = []
        for e in events:
            # 1 denotes start time.
            times.append([e[0], 1, e[2]])
            # 0 denotes end time.
            times.append([e[1] + 1, 0, e[2]])

        ans, max_value = 0, 0
        times.sort()

        for time_value in times:
            # If current time is a start time, find maximum sum of maximum end
            # time till now.
            if time_value[1]:
                ans = max(ans, time_value[2] + max_value)
            else:
                max_value = max(max_value, time_value[2])

        return ans
