"""leet 2661, medium"""


class Solution:
    """todo editorial"""

    def firstCompleteIndex(self, arr, mat):
        # Map to store the index of each number in the arr
        num_to_index = {}
        for i in range(len(arr)):
            num_to_index[arr[i]] = i

        result = float("inf")
        num_rows, num_cols = len(mat), len(mat[0])

        # Check for the earliest row to be completely painted
        for row in range(num_rows):
            # Tracks the greatest index in this row
            last_element_index = float("-inf")
            for col in range(num_cols):
                index_val = num_to_index[mat[row][col]]
                last_element_index = max(last_element_index, index_val)

            # Update result with the minimum index where this row is fully painted
            result = min(result, last_element_index)

        # Check for the earliest column to be completely painted
        for col in range(num_cols):
            last_element_index = float("-inf")
            for row in range(num_rows):
                index_val = num_to_index[mat[row][col]]
                last_element_index = max(last_element_index, index_val)

            # Update result with the minimum index where this column is fully painted
            result = min(result, last_element_index)

        return result
