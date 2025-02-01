"""leet 2658, medium"""


class Solution:
    """todo editorial"""

    # Helper function to count the number of fishes in a connected component
    def calculate_fishes(self, grid, visited, row, col):
        # Check boundary conditions, water cells, or already visited cells
        if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[0])
                or grid[row][col] == 0
                or visited[row][col]
        ):
            return 0

        # Mark the current cell as visited
        visited[row][col] = True

        # Accumulate the fish count from the current cell and its neighbors
        return (
                grid[row][col]
                + self.calculate_fishes(grid, visited, row, col + 1)
                + self.calculate_fishes(grid, visited, row, col - 1)
                + self.calculate_fishes(grid, visited, row + 1, col)
                + self.calculate_fishes(grid, visited, row - 1, col)
        )

    def findMaxFish(self, grid):
        rows, cols = len(grid), len(grid[0])
        max_fish_count = 0

        # A 2D list to track visited cells
        visited = [[False] * cols for _ in range(rows)]

        # Iterate through all cells in the grid
        for row in range(rows):
            for col in range(cols):
                # Start a DFS for unvisited land cells (fish available)
                if grid[row][col] > 0 and not visited[row][col]:
                    max_fish_count = max(
                        max_fish_count,
                        self.calculate_fishes(grid, visited, row, col),
                    )

        # Return the maximum fish count found
        return max_fish_count
