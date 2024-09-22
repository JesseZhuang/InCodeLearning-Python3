"""lint code 2448, hard"""
import heapq
import json
import sys
import threading


class MergeSort:
    has_been_called_in_sub_thread = False

    def __init__(self, nums):
        self.n = len(nums)
        self._temp = [0] * self.n
        self.nums = nums

    def sort(self):
        self.sort_range(0, self.n - 1)

    def sort_range(self, start, end):
        if threading.current_thread() is threading.main_thread():
            raise Exception('You should call sort_range in a sub thread.')
        MergeSort.has_been_called_in_sub_thread = True

        if start >= end: return

        self.sort_range(start, (start + end) // 2)
        self.sort_range((start + end) // 2 + 1, end)
        self.merge_range(start, end)

    def merge_range(self, start, end):
        middle = (start + end) // 2
        left_index = start
        right_index = middle + 1
        index = start

        while left_index <= middle and right_index <= end:
            if self.nums[left_index] <= self.nums[right_index]:
                self._temp[index] = self.nums[left_index]
                index += 1
                left_index += 1
            else:
                self._temp[index] = self.nums[right_index]
                index += 1
                right_index += 1

        while left_index <= middle:
            self._temp[index] = self.nums[left_index]
            index += 1
            left_index += 1

        while right_index <= end:
            self._temp[index] = self.nums[right_index]
            index += 1
            right_index += 1

        for i in range(start, end + 1):
            self.nums[i] = self._temp[i]


class Solution:

    def merge_sort_in_threadings(self, n, nums):
        """
        @param n: the number of child threads you need to use
        @param nums: an array of numbers
        @return: return sorted nums
        """
        size = (len(nums) - 1) // n + 1
        threads = []
        subarrays = []
        for i in range(n):
            start = i * size
            end = min(start + size - 1, len(nums) - 1)

            subarray = nums[start: end + 1]
            thread = threading.Thread(target=lambda: self.merge_sort(subarray))
            subarrays.append(subarray)

            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return self.merge_n_sorted_arrays(subarrays)

    def merge_sort(self, nums):
        instance = MergeSort(nums)
        instance.sort()

    # You can use this method to merge several ordered arrays
    def merge_n_sorted_arrays(self, arrays):
        result = []
        heap = []
        for index, array in enumerate(arrays):
            if len(array) == 0: continue
            heapq.heappush(heap, (array[0], index, 0))  # element, row_index, column_index

        while len(heap):
            val, x, y = heap[0]
            heapq.heappop(heap)
            result.append(val)
            if y + 1 < len(arrays[x]):
                heapq.heappush(heap, (arrays[x][y + 1], x, y + 1))

        return result


if __name__ == "main":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    input_file = open(input_path, 'r')
    output_file = open(output_path, 'w')

    n = json.loads(input_file.readline())
    nums = json.loads(input_file.readline())
    input_file.close()

    solution = Solution()
    sorted_nums = solution.merge_sort_in_threadings(n, nums)

    if not MergeSort.has_been_called_in_sub_thread:
        raise Exception('You should call sort_range in a sub thread.')

    output_file.write(json.dumps(sorted_nums))
    output_file.close()
