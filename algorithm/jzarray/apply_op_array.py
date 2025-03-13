"""leet 2460, easy"""


class Solution:
    """todo editorial"""

    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        write_index = 0  # Pointer to place non-zero elements

        for index in range(n):
            # Step 1: Merge adjacent equal elements if they are non-zero
            if (
                    index < n - 1
                    and nums[index] == nums[index + 1]
                    and nums[index] != 0
            ):
                nums[index] *= 2
                nums[index + 1] = 0
            # Step 2: Shift non-zero elements to the front
            if nums[index] != 0:
                if index != write_index:
                    nums[index], nums[write_index] = (
                        nums[write_index],
                        nums[index],
                    )
                write_index += 1
        return nums
