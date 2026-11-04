"""leet 1718, medium"""


class Solution:
    """Build the lexicographically largest distanced sequence by backtracking."""

    def constructDistancedSequence(self, target_number: int) -> list[int]:
        """Return a valid sequence, trying larger values before smaller ones.

        Time: O(n * n!) in the conservative worst case; there are at most n!
        partial placement orders, each trying or skipping up to n values/slots.
        Space: O(n) for the result, used-number table, and recursion stack.
        """
        # Initialize the result sequence with size 2*n - 1 filled with 0s
        result_sequence = [0] * (target_number * 2 - 1)

        # Keep track of which numbers are already placed in the sequence
        is_number_used = [False] * (target_number + 1)

        # Start recursive backtracking to construct the sequence
        self.find_lexicographically_largest_sequence(
            0, result_sequence, is_number_used, target_number
        )

        return result_sequence

    # Recursive function to generate the desired sequence
    def find_lexicographically_largest_sequence(
            self, current_index, result_sequence, is_number_used, target_number
    ):
        # If we have filled all positions, return true indicating success
        if current_index == len(result_sequence):
            return True

        # If the current position is already filled, move to the next index
        if result_sequence[current_index] != 0:
            return self.find_lexicographically_largest_sequence(
                current_index + 1,
                result_sequence,
                is_number_used,
                target_number,
            )

        # Descending choices make the first complete solution lexicographically
        # largest. In the worst case this explores O(n!) placement orders.
        for number_to_place in range(target_number, 0, -1):
            if is_number_used[number_to_place]:
                continue

            is_number_used[number_to_place] = True
            result_sequence[current_index] = number_to_place

            # If placing number 1, move to the next index directly
            if number_to_place == 1:
                if self.find_lexicographically_largest_sequence(
                        current_index + 1,
                        result_sequence,
                        is_number_used,
                        target_number,
                ):
                    return True
            # Place larger numbers at two positions if valid
            elif (
                    current_index + number_to_place < len(result_sequence)
                    and result_sequence[current_index + number_to_place] == 0
            ):
                result_sequence[current_index + number_to_place] = (
                    number_to_place
                )

                if self.find_lexicographically_largest_sequence(
                        current_index + 1,
                        result_sequence,
                        is_number_used,
                        target_number,
                ):
                    return True

                # Undo the placement for backtracking
                result_sequence[current_index + number_to_place] = 0

            # Undo current placement and mark the number as unused
            result_sequence[current_index] = 0
            is_number_used[number_to_place] = False

        return False
