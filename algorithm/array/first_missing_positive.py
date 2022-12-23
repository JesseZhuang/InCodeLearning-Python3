'''
variant of leetcode 41
Write a function:
def solution(A)
that, given an array A of N integers, returns the
smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''


def first_missing_positive_set(nums: list[int]) -> int:
    '''O(n) time and space, using set. 308 ms, 28.6MB'''
    seen = set()
    for num in nums:
        if num not in seen and 0 < num <= len(nums):
            seen.add(num)
    for i in range(1, len(nums)+1):
        if i not in seen:
            return i
    return len(nums) + 1


def solution(nums):
    '''swap in place, O(n) time, O(1) space (modifying input). 993 ms, 27.2 Mb.'''
    for i, num in enumerate(nums):
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        while 0 < nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
            swap(nums, i, nums[i]-1)
            # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] not swapping: bug
    for i, num in enumerate(nums):
        if num != i+1:
            return i+1
    return len(nums) + 1


solution([3, 4, -1, 1])  # buggy swap
