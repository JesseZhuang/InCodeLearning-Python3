"""leet 2594, medium"""
from collections import Counter


class Solution:
    """todo editorial, 1127 ms, 21.95 mb."""

    def repairCars(self, ranks: list[int], cars: int) -> int:
        # The minimum possible time is 1,
        # and the maximum possible time is when the slowest mechanic (highest rank) repairs all cars.
        low, high = 1, cars * cars * ranks[0]

        # Perform binary search to find the minimum time required.
        while low < high:
            mid = (low + high) // 2
            cars_repaired = sum(int((mid / rank) ** 0.5) for rank in ranks)

            # If the total cars repaired is less than required, increase the time.
            if cars_repaired < cars:
                low = mid + 1
            else:
                high = mid  # Otherwise, try a smaller time.

        return low


class Solution:
    """todo editorial, 503 ms, 21.69 mb"""

    def repairCars(self, rank: list[int], cars: int) -> int:
        # Count the frequency of each rank using a Counter
        count = Counter(rank)

        # Create a Min-heap storing [time, rank, n, count]:
        # - time: time for the next repair
        # - rank: mechanic's rank
        # - n: cars repaired by this mechanic
        # - count: number of mechanics with this rank
        # Initial time = rank (as rank * 1^2 = rank)
        min_heap = [[rank, rank, 1, count[rank]] for rank in count]
        heapify(min_heap)

        # Process until all cars are repaired
        while cars > 0:
            # Pop the mechanic with the smallest current repair time
            time, rank, n, count = heappop(min_heap)

            # Deduct the number of cars repaired by this mechanic group
            cars -= count

            # Increment the number of cars repaired by this mechanic
            n += 1

            # Push the updated repair time back into the heap
            # The new repair time is rank * n^2 (since time increases quadratically with n)
            heappush(min_heap, [rank * n * n, rank, n, count])

        return time
