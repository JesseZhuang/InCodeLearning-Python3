"""leet 2503, medium"""

from queue import PriorityQueue


class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        row_count, col_count = len(grid), len(grid[0])
        result = [0] * len(queries)
        # Directions for movement (right, down, left, up)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Store queries along with their original indices to restore order
        # later
        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])

        # Min-heap (priority queue) to process cells in increasing order of
        # value
        min_heap = PriorityQueue()
        visited = [[False] * col_count for _ in range(row_count)]
        # Keeps track of the number of cells processed
        total_points = 0
        # Start from the top-left cell
        min_heap.put((grid[0][0], 0, 0))
        visited[0][0] = True

        # Process queries in sorted order
        for query_value, query_index in sorted_queries:
            # Expand the cells that are smaller than the current query value
            while not min_heap.empty() and min_heap.queue[0][0] < query_value:
                cellValue, current_row, current_col = min_heap.get()

                # Increment count of valid cells
                total_points += 1

                # Explore all four possible directions
                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = (
                        current_row + row_offset,
                        current_col + col_offset,
                    )

                    # Check if the new cell is within bounds and not visited
                    if (
                            new_row >= 0
                            and new_col >= 0
                            and new_row < row_count
                            and new_col < col_count
                            and not visited[new_row][new_col]
                    ):
                        min_heap.put((grid[new_row][new_col], new_row, new_col))
                        # Mark as visited
                        visited[new_row][new_col] = True
            # Store the result for this query
            result[query_index] = total_points

        return result
