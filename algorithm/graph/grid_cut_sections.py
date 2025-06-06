"""leet 3394, medium"""


class Solution:
    """todo editorial"""

    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        # Check if valid cuts can be made in a specific dimension
        def _check_cuts(rectangles: list[list[int]], dim: int) -> bool:
            gap_count = 0

            # Sort rectangles by their starting coordinate in the given dimension
            rectangles.sort(key=lambda rect: rect[dim])

            # Track the furthest ending coordinate seen so far
            furthest_end = rectangles[0][dim + 2]

            for i in range(1, len(rectangles)):
                rect = rectangles[i]

                # If current rectangle starts after the furthest end we've seen,
                # we found a gap where a cut can be made
                if furthest_end <= rect[dim]:
                    gap_count += 1

                # Update the furthest ending coordinate
                furthest_end = max(furthest_end, rect[dim + 2])

            # We need at least 2 gaps to create 3 sections
            return gap_count >= 2

        # Try both horizontal and vertical cuts
        return _check_cuts(rectangles, 0) or _check_cuts(rectangles, 1)
