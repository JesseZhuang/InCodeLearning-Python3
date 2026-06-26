from collections import deque


class Solution:
    """752. Open the Lock - BFS"""

    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:  # O(10^4) states max
            state, turns = queue.popleft()
            for i in range(4):  # O(4) digits
                digit = int(state[i])
                for d in (-1, 1):  # O(2) directions
                    new_digit = (digit + d) % 10
                    new_state = state[:i] + str(new_digit) + state[i + 1:]
                    if new_state == target:
                        return turns + 1
                    if new_state not in visited and new_state not in dead:
                        visited.add(new_state)
                        queue.append((new_state, turns + 1))
        return -1


class SolutionBidirectional:
    """752. Open the Lock - Bidirectional BFS"""

    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        front, back = {"0000"}, {target}
        visited = {"0000", target}
        turns = 0

        while front and back:
            if len(front) > len(back):  # always expand smaller set
                front, back = back, front
            next_front = set()
            for state in front:  # O(|front|) per level
                for i in range(4):  # O(4) digits
                    digit = int(state[i])
                    for d in (-1, 1):  # O(2) directions
                        new_state = state[:i] + str((digit + d) % 10) + state[i + 1:]
                        if new_state in back:
                            return turns + 1
                        if new_state not in visited and new_state not in dead:
                            visited.add(new_state)
                            next_front.add(new_state)
            front = next_front
            turns += 1
        return -1
