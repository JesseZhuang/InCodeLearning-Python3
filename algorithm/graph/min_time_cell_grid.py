"""leet 2577 hard"""
import heapq


# Checks if given cell coordinates are valid and unvisited
def _is_valid(visited, row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols and (row, col) not in visited


class Solution:
    """todo editorial, mn*log(mn), mn"""

    def minimumTime(self, grid: list[list[int]]) -> int:
        # If both initial moves require more than 1 second, impossible to proceed
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        # Possible movements: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        # Priority queue stores (time, row, col)
        # Ordered by minimum time to reach each cell
        pq = [(grid[0][0], 0, 0)]

        while pq:
            time, row, col = heapq.heappop(pq)

            # Check if reached target
            if (row, col) == (rows - 1, cols - 1):
                return time

            # Skip if cell already visited
            if (row, col) in visited:
                continue
            visited.add((row, col))

            # Try all four directions
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy

                if not _is_valid(visited, next_row, next_col, rows, cols):
                    continue

                # Calculate the wait time needed to move to the next cell
                wait_time = (
                    1 if (grid[next_row][next_col] - time) % 2 == 0 else 0
                )
                next_time = max(grid[next_row][next_col] + wait_time, time + 1)
                heapq.heappush(pq, (next_time, next_row, next_col))

        return -1
