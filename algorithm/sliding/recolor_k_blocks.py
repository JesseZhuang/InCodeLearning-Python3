"""leet 2379, easy"""


class Solution:
    """todo editorial"""

    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        num_whites = 0
        num_recolors = float("inf")

        # Move right pointer
        for right in range(len(blocks)):

            # Increment num_whites if block at right pointer is white
            if blocks[right] == "W":
                num_whites += 1

            # k consecutive elements are found
            if right - left + 1 == k:

                # Update minimum
                num_recolors = min(num_recolors, num_whites)

                # Decrement num_whites if block at left pointer is white
                if blocks[left] == "W":
                    num_whites -= 1

                # Move left pointer
                left += 1

        return num_recolors
