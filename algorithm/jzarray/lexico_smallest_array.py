"""leet 2948, medium"""
from collections import deque


class Solution:
    """todo editorial"""

    def lexicographicallySmallestArray(self, nums, limit):
        nums_sorted = sorted(nums)

        curr_group = 0
        num_to_group = {}
        num_to_group[nums_sorted[0]] = curr_group

        group_to_list = {}
        group_to_list[curr_group] = deque([nums_sorted[0]])

        for i in range(1, len(nums)):
            if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                # new group
                curr_group += 1

            # assign current element to group
            num_to_group[nums_sorted[i]] = curr_group

            # add element to sorted group deque
            if curr_group not in group_to_list:
                group_to_list[curr_group] = deque()
            group_to_list[curr_group].append(nums_sorted[i])

        # iterate through input and overwrite each element with the next element in its corresponding group
        for i in range(len(nums)):
            num = nums[i]
            group = num_to_group[num]
            nums[i] = group_to_list[group].popleft()

        return nums
