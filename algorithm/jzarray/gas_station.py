"""LeetCode 134, medium, tags: array, greedy.

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next
(i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

Constraints:

n == gas.length == cost.length
1 <= n <= 10^5
0 <= gas[i], cost[i] <= 10^4
"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """One-pass greedy. O(n) time, O(1) space."""
        total_gain = 0
        curr_gain = 0
        answer = 0
        for i in range(len(gas)):  # O(n)
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]
            if curr_gain < 0:
                answer = i + 1
                curr_gain = 0
        return answer if total_gain >= 0 else -1


class Solution2:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """Brute force simulation. O(n^2) time, O(1) space."""
        n = len(gas)
        for start in range(n):  # O(n) outer
            tank = 0
            complete = True
            for j in range(n):  # O(n) inner, together O(n^2)
                idx = (start + j) % n
                tank += gas[idx] - cost[idx]
                if tank < 0:
                    complete = False
                    break
            if complete:
                return start
        return -1
