"""leet code 2924"""


class Solution:
    """todo editorial"""

    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        # Initialize the indegree array to track the number of incoming edges for each team
        indegree = [0] * n

        # Store the indegree of each team
        for edge in edges:
            indegree[edge[1]] += 1

        champ = -1
        champ_count = 0

        # Iterate through all teams to find those with an indegree of 0
        for i in range(n):
            # If the team can be a champion, store the team number and increment the count
            if indegree[i] == 0:
                champ_count += 1
                champ = i

        # If more than one team can be a champion, return -1, otherwise return the champion team number
        return champ if champ_count == 1 else -1
