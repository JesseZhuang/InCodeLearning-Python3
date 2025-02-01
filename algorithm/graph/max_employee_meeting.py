"""leet 2127, hard"""


class Solution:
    """todo editorial"""

    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_degree = [0] * n

        # Calculate in-degree for each node
        for person in range(n):
            in_degree[favorite[person]] += 1

        # Topological sorting to remove non-cycle nodes
        q = deque()
        for person in range(n):
            if in_degree[person] == 0:
                q.append(person)
        depth = [1] * n  # Depth of each node

        while q:
            current_node = q.popleft()
            next_node = favorite[current_node]
            depth[next_node] = max(depth[next_node], depth[current_node] + 1)
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)

        longest_cycle = 0
        two_cycle_invitations = 0

        # Detect cycles
        for person in range(n):
            if in_degree[person] == 0:  # Already processed
                continue

            cycle_length = 0
            current = person
            while in_degree[current] != 0:
                in_degree[current] = 0  # Mark as visited
                cycle_length += 1
                current = favorite[current]

            if cycle_length == 2:
                # For 2-cycles, add the depth of both nodes
                two_cycle_invitations += depth[person] + depth[favorite[person]]
            else:
                longest_cycle = max(longest_cycle, cycle_length)

        return max(longest_cycle, two_cycle_invitations)
