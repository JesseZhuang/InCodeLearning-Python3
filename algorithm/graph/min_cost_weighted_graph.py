"""leet 3108, hard"""


class Solution:
    """todo editorial"""

    def minimumCost(self, n, edges, queries):
        # Create the adjacency list of the graph
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))

        visited = [False] * n

        # Array to store the component ID of each node
        components = [0] * n
        component_cost = []

        component_id = 0

        # Perform DFS for each unvisited node to identify components and calculate their costs
        for node in range(n):
            if not visited[node]:
                # Get the component cost and mark all nodes in the component
                component_cost.append(
                    self._get_component_cost(
                        node, adj_list, visited, components, component_id
                    )
                )
                component_id += 1

        result = []
        for query in queries:
            start, end = query

            if components[start] == components[end]:
                # If they are in the same component, return the precomputed cost for the component
                result.append(component_cost[components[start]])
            else:
                # If they are in different components, return -1
                result.append(-1)

        return result

    # Helper function to calculate the cost of a component using BFS
    def _get_component_cost(
            self, node, adj_list, visited, components, component_id
    ):

        # Initialize the cost to the number that has only 1s in its binary representation
        current_cost = -1

        # Mark the node as part of the current component
        components[node] = component_id
        visited[node] = True

        # Explore all neighbors of the current node
        for neighbor, weight in adj_list[node]:
            # Update the component cost by performing a bitwise AND of the edge weights
            current_cost &= weight
            if not visited[neighbor]:
                # Recursively calculate the cost of the rest of the component
                # and accumulate it into currentCost
                current_cost &= self._get_component_cost(
                    neighbor, adj_list, visited, components, component_id
                )

        return current_cost
