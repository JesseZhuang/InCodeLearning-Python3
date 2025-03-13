"""leet 2698, medium"""


class Solution:
    """todo editorial"""

    def can_partition(self, string_num, target):
        # Valid Partition Found
        if not string_num and target == 0:
            return True

        # Invalid Partition Found
        if target < 0:
            return False

        # Recursively check all partitions for a valid partition
        for index in range(len(string_num)):
            left = string_num[: index + 1]
            right = string_num[index + 1:]
            left_num = int(left)

            if self.can_partition(right, target - left_num):
                return True

        return False

    def punishmentNumber(self, n: int) -> int:
        punishment_num = 0

        # Iterate through numbers in range [1, n]
        for current_num in range(1, n + 1):
            square_num = current_num * current_num

            # Check if valid partition can be found and add squared number if so
            if self.can_partition(str(square_num), current_num):
                punishment_num += square_num

        return punishment_num
