"""leet 827, hard"""


class Solution:
    """todo editorial"""

    def largestIsland(self, grid: list[list[int]]) -> int:
        island_sizes = {}
        island_id = 2

        # Step 1: Mark all islands and calculate their sizes
        for current_row in range(len(grid)):
            for current_column in range(len(grid[0])):
                if grid[current_row][current_column] == 1:
                    island_sizes[island_id] = self.explore_island(
                        grid, island_id, current_row, current_column
                    )
                    island_id += 1

        # If there are no islands, return 1
        if not island_sizes:
            return 1

        # If the entire grid is one island, return its size or size +
        if len(island_sizes) == 1:
            island_id -= 1
            return (
                island_sizes[island_id]
                if island_sizes[island_id] == len(grid) * len(grid[0])
                else island_sizes[island_id] + 1
            )

        max_island_size = 1

        # Step 2: Try converting every 0 to 1 and calculate the resulting island size
        for current_row in range(len(grid)):
            for current_column in range(len(grid[0])):
                if grid[current_row][current_column] == 0:
                    current_island_size = 1
                    neighboring_islands = set()

                    # Check down
                    if (
                            current_row + 1 < len(grid)
                            and grid[current_row + 1][current_column] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row + 1][current_column]
                        )

                    # Check up
                    if (
                            current_row - 1 >= 0
                            and grid[current_row - 1][current_column] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row - 1][current_column]
                        )

                    # Check right
                    if (
                            current_column + 1 < len(grid[0])
                            and grid[current_row][current_column + 1] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row][current_column + 1]
                        )

                    # Check left
                    if (
                            current_column - 1 >= 0
                            and grid[current_row][current_column - 1] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row][current_column - 1]
                        )

                    # Sum the sizes of all unique neighboring islands
                    for island_id in neighboring_islands:
                        current_island_size += island_sizes[island_id]
                    max_island_size = max(max_island_size, current_island_size)

        return max_island_size

    def explore_island(
            self,
            grid: list[list[int]],
            island_id: int,
            current_row: int,
            current_column: int,
    ) -> int:
        if (
                current_row < 0
                or current_row >= len(grid)
                or current_column < 0
                or current_column >= len(grid[0])
                or grid[current_row][current_column] != 1
        ):
            return 0

        grid[current_row][current_column] = island_id

        return (
                1
                + self.explore_island(
            grid, island_id, current_row + 1, current_column
        )
                + self.explore_island(
            grid, island_id, current_row - 1, current_column
        )
                + self.explore_island(
            grid, island_id, current_row, current_column + 1
        )
                + self.explore_island(
            grid, island_id, current_row, current_column - 1
        )
        )
